# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v15] - 2026-06-08

### Added
- **Autonomous Orchestrator Agent v2** (`autonomous_orchestrator`): The most advanced meta-agent in the system. Supports long-running, multi-session autonomous missions with:
  - Automatic dated mission folder creation (`/home/workdir/artifacts/missions/`)
  - Structured `state.json` persistence (milestones, reflections, decisions, artifacts)
  - Robust resume capability across conversations
  - Mandatory reflection after every major step
  - Professional error recovery and replanning
- 5 new mission persistence helper functions:
  - `create_mission(goal)`
  - `save_mission_state(mission_path, state)`
  - `load_mission_state(mission_path)`
  - `get_mission_summary(mission_path)`
  - `sanitize_mission_slug(text)`
- Full production-ready persistence protocol documented in the agent's system prompt.

### Changed
- Now **15 agents** total (v15).
- `Chief of Staff` system prompt updated to include awareness of the new Autonomous Orchestrator.
- `load_all_agents()` now reports v15 and 15 agents.
- Single-file version (`TailorMade_Agents_v15.py`) is the recommended canonical implementation.
- Updated documentation and examples for autonomous mission workflows.

### Improved
- Better long-horizon project support (research + code + analysis + visuals + legal in one persistent mission).
- Stronger emphasis on professional project organization (state tracking, reflections, FINAL_REPORT.md).

---

## [v14] - 2026-06-05

### Added
- **Study Strategist Agent (SSA)**: Expert exam preparation coach specialized in Brazilian public contests (Vunesp, TJ-SP, etc.). Includes personalized study plans, high-quality practice question generation, and spaced repetition scheduling.
- **Contract Intelligence Agent (CIA)**: Specialized commercial contract reviewer focused on risk analysis, clause review, and Brazilian law compliance.

### Changed
- Full 14-agent system now complete and production-ready.
- `TailorMade_Agents_v14_SingleFile.py` is now the recommended self-contained file.
- Repository cleanup: Removed duplicate files, `__pycache__`, and improved `.gitignore`.
- All agent definitions (including the original 10) now have complete, detailed `system_prompt`s.

### Improved
- Better documentation and consistent structure across all files.
- `test_agents.py` now validates all 14 agents properly.
- Cleaner project structure for easier use with Grok.

---

## [v12] - 2026-06

### Added
- **Due Diligence Agent (DDA)**: Investment research and fundamental analysis agent.
- **Political Analysis Agent (PAA)**: Domestic politics and power dynamics analysis (strong focus on Brazil & Latin America).

---

## [v10] - 2026-05

### Added
Initial release with 10 core agents:

- Deep Research Agent (DRA)
- CodeForge Agent
- VisualCraft Agent
- Narrative Weaver Agent
- Quant Analyst Agent
- Automation Orchestrator Agent
- Brazilian Cultural Agent
- Chief of Staff (Meta-Agent)
- Geopolitical Intelligence Agent (GIA)
- News Monitor Agent

---

## [Unreleased]

### Planned
- Additional specialized agents if needed
- Enhanced examples and multi-agent workflow templates
