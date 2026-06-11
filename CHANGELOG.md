# Tailor-Made Agents Changelog

All notable changes to the Tailor-Made Agents registry are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v16] - 2026-06-11

### Added

- **Structured Metadata Layer**
  - Global `REGISTRY_META` dictionary with version, description, and category information.
  - Per-agent `"metadata"` block containing:
    - `version`
    - `category` (`core`, `orchestration`, or `domain_intelligence`)
    - `tags` (searchable keywords)
    - `last_updated`
    - `complexity` (`medium` or `high`)
  - New helper functions:
    - `get_agent_metadata(agent_key)`
    - `list_agents_by_category(category)`
    - `get_registry_summary()`

- **Validation System**
  - `validate_registry()` — validates that all agents contain required keys and proper metadata.
  - Automatic validation option in `load_all_agents(validate=True)`.
  - Clear error/warning reporting for missing fields or misconfigured metadata.

- **Three-Tier Agent Categorization**
  - `core` — Foundational specialist agents (research, code, visuals, writing, quant, Brazil cultural).
  - `orchestration` — Meta-coordination agents (`automation_orchestrator`, `chief_of_staff`, `autonomous_orchestrator`).
  - `domain_intelligence` — Specialized domain agents (geopolitics, news, due diligence, politics, study, contracts).

- **Orchestration Hierarchy Improvements (Option B)**
  - Major enhancement to the `chief_of_staff` system prompt with a clear decision framework.
  - Added **Step 0 — Goal Signal Analysis**: The model now first detects long-horizon vs. complex single-session signals before choosing an orchestration mode.
  - Explicit decision tree distinguishing when to use:
    - `autonomous_orchestrator` (long-horizon, persistence, multi-session, mission folders)
    - `automation_orchestrator` (complex single-session workflows)
    - `chief_of_staff` (strategic decisions, team composition, synthesis)
  - Added `recommend_orchestration_mode(goal)` helper function that implements the same logic externally.

- **New Helper Function**
  - `recommend_orchestration_mode(goal: str)` — Analyzes a goal description and returns the recommended orchestration mode along with reasoning.

### Changed

- `chief_of_staff` system prompt grew significantly (from ~1,308 to 3,844 characters) to include the full orchestration hierarchy and goal signal analysis logic.
- `load_all_agents()` now supports a `validate` parameter and shows category information when printing.
- Improved documentation and structure throughout the file header.
- All original agent definitions, mission persistence helpers, and Autonomous Orchestrator v2 behavior remain fully intact.

### Fixed

- Fixed issues in the initial v16 generator script (broken function definitions, duplicate `load_all_agents`, incorrect complexity expressions).
- Ensured clean module import and validation on load.

### Improved

- **News Monitor Agent (`news_monitor`)**
  - Significantly revised system prompt (v1.2)
  - Added explicit **Quantity Guidance** section to remove bias toward small fixed numbers of developments
  - Instructs the model to return *all meaningfully relevant developments* and explicitly allows 6–12+ items on high-volume days
  - Added required **`Implications`** field (Market / Geopolitical / Sector / Portfolio relevance)
  - Made **`Why it matters`** required on every development
  - Added explicit handling for **"No Significant Developments"** days
  - Improved guidance on source conflict resolution and prioritization of market/geopolitical implications
  - Updated metadata to `version: "1.2"`

### Notes

- Full backward compatibility with v15 usage patterns is maintained.
- The file size increased to ~62 KB primarily due to richer metadata and the significantly expanded `chief_of_staff` prompt.
- The orchestration improvements make the distinction between the three meta-agents much clearer and more actionable.
- The News Monitor Agent is now significantly more useful for investment and geopolitical analysis workflows.

---

## [v15] - Previous Version

- Original single-file agent registry with 15 agents.
- Included Autonomous Orchestrator v2 with mission folder persistence and structured state management.
- Strong support for Brazil/LatAm, geopolitics, investing, and long-running autonomous tasks.
- No structured metadata or validation layer.
- Overlapping orchestration responsibilities between `automation_orchestrator`, `chief_of_staff`, and `autonomous_orchestrator` (addressed in v16).

---

## Roadmap / Future Ideas

- Add a lightweight `route_request()` or orchestration router helper.
- Further refine `chief_of_staff` to optionally output its mode decision explicitly.
- Consider adding agent composition helpers (e.g., `activate_team([...])`).
- Explore a shorter "core protocol" version of the Autonomous Orchestrator prompt for very long contexts.
- Add optional integration hooks with the memory system.

---

**Current recommended file:** `TailorMade_Agents_v16.py` (located in `/home/workdir/artifacts/agents/`)