import json
import time
from datetime import date, datetime
from pathlib import Path

import requests


SYMBOL = "0050"
START_DATE = "2026-07-29"

OUTPUT = Path("data/0050.json")


def roc_to_ad(value):
    """115/07/29 -> 2026-07-29"""

    parts = value.split("/")

    year = int(parts[0]) + 1911
    month = int(parts[1])
    day = int(parts[2])

    return f"{year:04d}-{month:02d}-{day:02d}"


def fetch_month(year, month):

    url = (
        "https://www.twse.com.tw"
        "/rwd/zh/afterTrading/STOCK_DAY"
    )

    params = {
        "date": f"{year}{month:02d}01",
        "stockNo": SYMBOL,
        "response": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    result = response.json()

    if result.get("stat") != "OK":

        print(
            f"{year}-{month:02d}: "
            f"{result.get('stat')}"
        )

        return []

    rows = []

    for row in result.get("data", []):

        if len(row) < 7:
            continue

        try:

            trade_date = roc_to_ad(row[0])

            close = float(
                str(row[6])
                .replace(",", "")
            )

            rows.append({
                "date": trade_date,
                "close": close
            })

        except Exception as error:

            print(
                "Skip row:",
                row,
                error
            )

    return rows


def main():

    today = date.today()

    # 從 2026/07 開始抓到目前月份
    year = 2026
    month = 7

    all_data = []

    while (
        year < today.year
        or (
            year == today.year
            and month <= today.month
        )
    ):

        print(
            f"Fetching {year}-{month:02d}"
        )

        try:

            rows = fetch_month(
                year,
                month
            )

            all_data.extend(rows)

        except Exception as error:

            print(
                "Request failed:",
                error
            )

        time.sleep(1)

        if month == 12:

            year += 1
            month = 1

        else:

            month += 1


    # 去除重複日期
    unique = {}

    for row in all_data:

        if row["date"] >= START_DATE:

            unique[row["date"]] = row


    data = sorted(
        unique.values(),
        key=lambda x: x["date"]
    )


    if not data:

        raise RuntimeError(
            "No 0050 data found"
        )


    # 必須找到 7/29
    if not any(
        row["date"] == START_DATE
        for row in data
    ):

        raise RuntimeError(
            "2026-07-29 price not found"
        )


    output = {
        "symbol": SYMBOL,
        "name": "元大台灣50",
        "updatedAt": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "data": data
    }


    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    OUTPUT.write_text(
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


    print(
        f"Saved {len(data)} records"
    )

    print(
        f"Output: {OUTPUT}"
    )


if __name__ == "__main__":
    main()