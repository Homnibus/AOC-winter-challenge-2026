# Iteration Log

## 2026-03-14

- Setup initial Python workspace and Copilot agent instructions.
- Added baseline strategy placeholder with deterministic fallback.
- Added first regression safety test.
- Integrated official local simulator repository in `external/`.
- Wired simulator runner to use `src/main.py` by default.
- Added PowerShell scripts for local run and mirror mode.
- Added persistent context file `notes/project-context.md` and linked it in global Copilot instructions.
- Added `notes/setup-roadmap.md` with phased checklist and Definition of Done.
- Set current focus to environment validation (venv, pytest/ruff/black, first complete local simulation).
- Configured Python interpreter and bootstrapped pip for it.
- Installed dev tools in active interpreter and validated: pytest=pass, ruff=pass, black --check=pass.
- Fixed `scripts/run-local-sim.ps1` Maven bootstrap guard for missing `bin\\mvn.cmd`.
- Ran local simulation script and exposed viewer URL (`http://localhost:8888`).
- Added headless simulation reporter (`external/.../LocalReportMain.java`, `scripts/run-local-report.ps1`).
- Verified concrete local result against Boss with scores and outcome printed in terminal.
- Added single-file bot builder (`scripts/build_single_file.py`, `scripts/build-codingame-singlefile.ps1`) outputting `dist/codingame_bot.py`.
- Generated clickable report files in `notes/reports/` and validated both modular bot and single-file bot against Boss.
- Added regression tests: empty body parsing, blocked preferred move fallback, boxed-in command emission.
- Added explicit gravity priority in roadmap strategy and context.
- Ran full quality gate: pytest=7 passed, ruff=pass, black --check=pass.
- Prepared PR review draft in `notes/pr-proposal-v0.md`.
- Introduced Scrum-style prioritized backlog in `notes/backlog.md`.
- Kept `notes/setup-roadmap.md` as legacy pointer for compatibility.
- Updated README with concise differences between sim/mirror/report scripts.
- Expanded PR draft with explicit installation/simulation setup details.
- Removed legacy roadmap file (`notes/setup-roadmap.md`) to standardize on `notes/backlog.md`.
- Removed viewer/mirror scripts and kept one configurable headless simulation script (`scripts/run-local-report.ps1`).
- Added AI/mode-agent disclaimer in project docs/backlog.
- Fixed `run-local-report.ps1` parameter block placement (PowerShell parsing) and validated end-to-end run.
- Added official Codingame Python starter snapshot in `notes/codingame-python-starter-reference.py`.
- Performed readability pass on `src/game_state.py`, `src/main.py`, `src/strategy.py` while preserving baseline behavior.
