# AGENTS.md

## Repository overview

This repository is a small static website with supporting Python scripts and data files.

Key areas:
- `index.html`: main website UI and client-side logic.
- `scripts/`: maintenance/data update scripts.
- `data/`: generated or maintained data consumed by the site.
- `.github/workflows/`: GitHub Actions automation.

## Working rules

- Keep changes minimal and focused on the GitHub issue.
- Preserve the existing static-site architecture unless the issue explicitly requires a larger change.
- Do not introduce new dependencies unless they are necessary.
- Do not modify unrelated files.
- Preserve existing GitHub Pages deployment and data-update workflows unless the issue explicitly requires changes to them.
- When changing Python scripts, keep them compatible with the repository's existing execution environment.
- When changing frontend behavior, verify the resulting HTML/JavaScript remains valid and the page can still load without a build step.

## Before finishing

- Inspect the diff for unrelated changes.
- Run any relevant checks or scripts available for the files you changed.
- If no automated test exists, perform the most appropriate lightweight validation and describe it in the pull request.
