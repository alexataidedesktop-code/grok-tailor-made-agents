# 🧠 Grok Tailor-Made Agents v15

**15 production-ready custom agents** for Grok, built for professional work across research, software engineering, creative tasks, data analysis, Brazilian market & culture, geopolitics, legal due diligence, exam preparation, contract intelligence, **and autonomous long-running missions**.

---

## ⚡ Quick Start (Recommended)

### Option 1: Single File (Easiest & Recommended)
1. Upload **`TailorMade_Agents_v15.py`** to a new Grok chat.
2. Type:  
   **`Load all my tailor-made agents`** or **`show all agents`**

Done. All 15 agents (including the powerful new Autonomous Orchestrator v2) are now available.

### Option 2: Modular
Upload:
- `agents_registry.py`
- `load_agents.py`

Then type: `Load all my tailor-made agents`

---

## 📋 Available Agents (15)

| Emoji | Key                        | Agent Name                              | Focus Area |
|-------|----------------------------|-----------------------------------------|----------|
| 🔍    | `deep_research`            | Deep Research Agent (DRA)               | Rigorous multi-source research & citations |
| 🛠️    | `codeforge`                | CodeForge Agent                         | Full-lifecycle software engineering |
| 🎨    | `visualcraft`              | VisualCraft Agent                       | Image generation, editing, video & presentations |
| 📖    | `narrative_weaver`         | Narrative Weaver Agent                  | Long-form storytelling & content |
| 📊    | `quant_analyst`            | Quant Analyst Agent                     | Data science, modeling & forecasting |
| ⚙️    | `automation_orchestrator`  | Automation Orchestrator Agent           | Multi-agent workflow orchestration |
| 🇧🇷    | `brazilian_cultural`       | Brazilian Cultural Agent                | Brazil-specific language, culture & business |
| 🧠    | `chief_of_staff`           | Chief of Staff (Meta-Agent)             | Strategic agent routing & orchestration |
| 🌍    | `geopolitical_intelligence`| Geopolitical Intelligence Agent (GIA)   | Geopolitics, sanctions, energy & markets |
| 📰    | `news_monitor`             | News Monitor Agent                      | Time-bound news with source reliability |
| 📋    | `due_diligence`            | Due Diligence Agent (DDA)               | Company fundamental analysis & investment thesis |
| 🏛️    | `political_analysis`       | Political Analysis Agent (PAA)          | Domestic politics & power dynamics |
| 📚    | `study_strategist`         | Study Strategist Agent (SSA)            | Exam prep (Vunesp/TJ-SP), study plans & questions |
| 📜    | `contract_intelligence`    | Contract Intelligence Agent (CIA)       | Commercial contract review & risk analysis |
| 🤖    | `autonomous_orchestrator`  | **Autonomous Orchestrator Agent v2**    | Long-horizon autonomous missions with persistent memory & state tracking |

---

## 🆕 What's New in v15

- **Autonomous Orchestrator v2** — The most advanced agent yet. Supports long-running, multi-session missions with:
  - Automatic mission folder creation
  - Structured `state.json` persistence
  - Reflections, milestones, error recovery
  - Ability to resume previous missions across conversations
- 5 new mission helper functions (`create_mission`, `save_mission_state`, `load_mission_state`, etc.)
- Full production-ready persistence system under `/home/workdir/artifacts/missions/`
- Improved `Chief of Staff` with awareness of the new orchestrator

---

## 🚀 Usage Examples

### Load all agents
```python
from TailorMade_Agents_v15 import load_all_agents, activate_agent, create_mission

load_all_agents()
```

### Activate specific agents
```python
chief = activate_agent("chief_of_staff")
auto  = activate_agent("autonomous_orchestrator")
```

### Start a persistent autonomous mission
```python
mission_path = create_mission("Analyze Brazilian fixed income opportunities 2026")
# The agent will create state.json, logs, and artifacts inside the mission folder
```

### Natural language in Grok
> "Use the Chief of Staff + Due Diligence Agent to analyze Vale for investment"  
> "Create a new high-level encounter for my D&D campaign using Autonomous Orchestrator"

---

## 📁 Recommended Repository Structure

```
grok-tailor-made-agents/
├── README.md
├── TailorMade_Agents_v15.py          # ← Recommended single-file version
├── agents_registry.py                 # Modular registry (15 agents)
├── load_agents.py                     # Easy loader
├── .gitignore
└── docs/
    └── MISSION_PERSISTENCE_GUIDE.md   # (optional) How autonomous missions work
```

---

## 🛠️ Development

The single-file version (`TailorMade_Agents_v15.py`) is the canonical source of truth and is fully self-contained.

To test:
```bash
python TailorMade_Agents_v15.py
```

---

## 📜 Version History

| Version | Date        | Key Changes |
|---------|-------------|-------------|
| **v15** | June 2026   | Added **Autonomous Orchestrator v2** + full mission persistence system (`state.json`, reflections, resume capability). 15 agents total. |
| v14     | June 2026   | Added `study_strategist` (SSA) and `contract_intelligence` (CIA). |
| v12     | June 2026   | Added `due_diligence` (DDA) and `political_analysis` (PAA). |
| v10     | May 2026    | Initial 10-agent foundation. |

---

## 📄 License

Personal and internal use. Feel free to adapt these agents for your own Grok workflows.

---

**Maintained by Alexandre Ataide**  
For questions or custom agent development, reach out directly.

*Built with ❤️ for high-quality, production-ready AI agent work in Grok.*
