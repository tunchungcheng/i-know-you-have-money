# i-know-you-have-money
哲哲分析師 0050 資產追蹤網站 - 我知道你們還有錢

## 使用 Codex 處理 GitHub Issue

本專案改採直接從 Codex 處理 GitHub Issue，不再透過 GitHub Actions 呼叫 OpenAI API，因此不需要 `OPENAI_API_KEY`。

建議流程：

1. 在 GitHub 建立 Issue，清楚描述問題、預期行為與驗收條件。
2. 打開 Codex，選擇此 repository。
3. 指示 Codex：`Resolve GitHub issue #<issue-number>. Read and follow AGENTS.md, implement the fix, run relevant checks, and create a PR.`
4. Review Codex 產生的變更與測試結果。
5. Merge PR。

`AGENTS.md` 內包含本專案的固定工作規則，Codex 處理 Issue 時應先閱讀並遵守。
