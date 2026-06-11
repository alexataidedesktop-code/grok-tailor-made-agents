# Tailor-Made Agents v16

**Production-grade, self-contained agent registry for Grok**  
Strong support for deep research, software engineering, visual creation, financial modeling, Brazilian market & culture, geopolitics, due diligence, political analysis, exam preparation, contract review, and long-running autonomous missions.

**Current Version:** v16.0 (2026-06-11)  
**Recommended File:** `TailorMade_Agents_v16.py`  
**Total Agents:** 15  
**Status:** Production-ready

---

## What's New in v16

### Major Additions
- **Structured Metadata Layer** — Every agent now includes rich metadata (`version`, `category`, `tags`, `last_updated`, `complexity`). Global `REGISTRY_META` dictionary for registry-wide information.
- **Validation System** — `validate_registry()` automatically checks schema compliance. `load_all_agents(validate=True)` runs validation on import.
- **Three-Tier Categorization**
  - `core` — Foundational specialist agents
  - `orchestration` — Meta-coordination agents
  - `domain_intelligence` — Specialized domain experts
- **Orchestration Hierarchy Improvements (v16.1)**
  - Step 0 — Goal Signal Analysis (detects long-horizon vs complex single-session goals)
  - Explicit decision tree for choosing the right meta-agent
  - New helper: `recommend_orchestration_mode(goal)`
- **News Monitor Agent v1.2** — Significantly improved prompt with flexible quantity guidance, mandatory `Implications` field, and better handling of quiet news days.
- New helper functions: `get_agent_metadata()`, `list_agents_by_category()`, `get_registry_summary()`

Full details in [CHANGELOG.md](CHANGELOG.md).

---

## Agent Registry

### Core Specialist Agents (6)
| Emoji | Agent | Focus |
|-------|-------|-------|
| 🔍 | Deep Research Agent (DRA) | Multi-source verification, citation-backed synthesis |
| 🛠️ | CodeForge Agent | Full-lifecycle software engineering in sandbox |
| 🎨 | VisualCraft Agent | Image generation, editing, video, presentations |
| 📖 | Narrative Weaver Agent | Long-form storytelling, brand narratives, bilingual content |
| 📊 | Quant Analyst Agent | Data science, financial modeling, simulations, dashboards |
| 🇧🇷 | Portuguese-Brazilian Cultural Agent | Brazilian language, culture, business practices, localization |

### Orchestration & Meta Agents (3)
| Emoji | Agent | Focus |
|-------|-------|-------|
| ⚙️ | Automation Orchestrator Agent | Complex single-session workflow decomposition & coordination |
| 🧠 | Chief of Staff (Meta-Agent) | Strategic orchestration, team composition, quality synthesis |
| 🤖 | Autonomous Orchestrator Agent v2 | Long-horizon autonomous execution with persistent mission folders + state tracking |

### Domain Intelligence Agents (6)
| Emoji | Agent | Focus |
|-------|-------|-------|
| 🌍 | Geopolitical Intelligence Agent (GIA) | Geopolitics, sanctions, energy security, political risk (LatAm strength) |
| 📰 | News Monitor Agent | Time-bound news intelligence with source reliability ratings |
| 📋 | Due Diligence Agent (DDA) | Institutional-quality company & investment analysis |
| 🏛️ | Political Analysis Agent (PAA) | Domestic political context, power dynamics, scenario planning |
| 📚 | Study Strategist Agent (SSA) | Exam prep (Vunesp TJ-SP, public contests), study plans, question generation |
| 📜 | Contract Intelligence Agent (CIA) | Commercial contract review, risk analysis, redlines (Brazilian law) |

---

## Quick Start

### Load the Registry
```python
from TailorMade_Agents_v16 import load_all_agents, activate_agent

load_all_agents(validate=True)           # Recommended - validates + prints summary
```

### Activate a Specific Agent
```python
agent = activate_agent("chief_of_staff")
# or
agent = activate_agent("autonomous_orchestrator")
```

### Get Registry Information
```python
from TailorMade_Agents_v16 import (
    get_registry_summary,
    list_agents_by_category,
    get_agent_metadata,
    recommend_orchestration_mode
)

print(get_registry_summary())
core_agents = list_agents_by_category("core")
meta = get_agent_metadata("due_diligence")
mode = recommend_orchestration_mode("Build a persistent daily ANBIMA debenture monitoring system")
```

---

## Orchestration Hierarchy (v16.1)

The `chief_of_staff` now follows a clear decision framework:

1. **Step 0 — Goal Signal Analysis**
   - Long-horizon / persistence signals → `autonomous_orchestrator`
   - Complex single-session workflow → `automation_orchestrator`
   - Strategic / high-level / synthesis → `chief_of_staff` + specialists

2. Use `recommend_orchestration_mode(goal)` to get an external recommendation before starting large projects.

---

## Autonomous Orchestrator v2 — Mission Persistence

For long-running, multi-session goals:

```python
from TailorMade_Agents_v16 import (
    create_mission, save_mission_state, load_mission_state, get_mission_summary
)

mission_path = create_mission("Daily fixed income ranking report")
state = load_mission_state(mission_path)   # Resume if exists
# ... run mission ...
save_mission_state(mission_path, updated_state)
```

All state, artifacts, logs, and reports live inside dated mission folders under `/home/workdir/artifacts/missions/`.

---

## Validation & Quality

```python
from TailorMade_Agents_v16 import validate_registry

report = validate_registry()   # Returns detailed report dict
```

All 15 agents are validated on every load when `validate=True`.

---

## File Structure

```
agents/
├── TailorMade_Agents_v16.py      # Main self-contained registry (recommended)
├── CHANGELOG.md                  # Full version history
└── README.md                     # This file
```

---

## Updating Your Grok Chats

1. Upload `TailorMade_Agents_v16.py` to any new or existing Grok conversation.
2. Run `load_all_agents()` once at the start of the session.
3. The registry becomes immediately available for the entire conversation.

---

## Recommended Workflow

For simple tasks → Activate the specialist directly.  
For complex single-session work → Use `automation_orchestrator` or `chief_of_staff`.  
For long-horizon / resumable projects → Use `autonomous_orchestrator` + mission folders.

---

## License & Notes

This registry is designed for personal and professional use inside Grok.  
All agents are self-contained with embedded system prompts and tool permissions.

For questions, enhancements, or new agent requests, activate `chief_of_staff` or `autonomous_orchestrator` with your goal.

**Last Updated:** 2026-06-11  
**Registry Version:** v16.0

---

*Built for Alexandre Ataide’s custom Tailor-Made AI Agent ecosystem.*
