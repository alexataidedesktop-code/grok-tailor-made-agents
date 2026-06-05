# 🧠 Grok Tailor-Made Agents v14

**14 production-ready custom agents** for Grok, built for professional work across research, software engineering, creative tasks, data analysis, Brazilian market & culture, geopolitics, legal due diligence, exam preparation, and contract intelligence.

---

## ⚡ Quick Start (Recommended)

### Option 1: Single File (Easiest)
1. Upload **`TailorMade_Agents_v14_SingleFile.py`** to a new Grok chat.
2. Type:  
   **`Load all my tailor-made agents`**

Done. All 14 agents are now available in that conversation.

### Option 2: Modular (Best for development)
Upload both files:
- `agents_registry.py`
- `load_agents.py`

Then type: `Load all my tailor-made agents`

---

## 📋 Available Agents (14)

| Emoji | Key                        | Agent Name                              | Focus Area                              |
|-------|----------------------------|-----------------------------------------|-----------------------------------------|
| 🔍    | `deep_research`            | Deep Research Agent (DRA)               | Rigorous multi-source research & citations |
| 🛠️    | `codeforge`                | CodeForge Agent                         | Full-lifecycle software engineering     |
| 🎨    | `visualcraft`              | VisualCraft Agent                       | Image generation, editing & presentations |
| 📖    | `narrative_weaver`         | Narrative Weaver Agent                  | Long-form storytelling & content        |
| 📊    | `quant_analyst`            | Quant Analyst Agent                     | Data science, modeling & forecasting    |
| ⚙️    | `automation_orchestrator`  | Automation Orchestrator Agent           | Multi-agent workflow orchestration      |
| 🇧🇷    | `brazilian_cultural`       | Brazilian Cultural Agent                | Brazil-specific language, culture & business |
| 🧠    | `chief_of_staff`           | Chief of Staff (Meta-Agent)             | Strategic agent routing & orchestration |
| 🌍    | `geopolitical_intelligence`| Geopolitical Intelligence Agent (GIA)   | Geopolitics, sanctions, energy & markets |
| 📰    | `news_monitor`             | News Monitor Agent                      | Time-bound news with source reliability |
| 📋    | `due_diligence`            | Due Diligence Agent (DDA)               | Company fundamental analysis & investment thesis |
| 🏛️    | `political_analysis`       | Political Analysis Agent (PAA)          | Domestic politics & power dynamics      |
| 📚    | `study_strategist`         | Study Strategist Agent (SSA)            | Exam prep, study plans & practice questions (Vunesp/TJ-SP) |
| 📜    | `contract_intelligence`    | Contract Intelligence Agent (CIA)       | Commercial contract review & risk analysis |

---

## 🚀 Usage Examples

### Load everything
```python
from TailorMade_Agents_v14_SingleFile import load_all_agents, get_agent, activate_agent

load_all_agents()                    # Shows all 14 agents
```

### Activate specific agents
```python
chief = activate_agent("chief_of_staff")
dda   = activate_agent("due_diligence")
ssa   = activate_agent("study_strategist")
cia   = activate_agent("contract_intelligence")
```

### Use in Grok chat (after loading)
Just mention the agent naturally:
- "Use the Chief of Staff to plan this project"
- "Have the Due Diligence Agent analyze Vale"
- "Create a 60-day study plan with the Study Strategist for Escrevente TJ-SP"

---

## 📁 Repository Structure

```
grok-tailor-made-agents/
├── TailorMade_Agents_v14_SingleFile.py   # ← Recommended (self-contained)
├── agents_registry.py                     # Full modular registry (14 agents)
├── load_agents.py                         # Easy loader + pretty printing
├── test_agents.py                         # Validation tests (all 14 agents)
└── README.md
```

---

## 🛠️ Development & Testing

Run the full test suite:
```bash
python test_agents.py
```

Expected output: All tests pass with **14 agents** loaded and validated.

---

## 📜 Version History

| Version | Date       | Changes |
|---------|------------|---------|
| **v14** | June 2026  | Added `study_strategist` (SSA) and `contract_intelligence` (CIA). Full 14-agent set with complete system prompts. Improved single-file experience. |
| v12     | June 2026  | Added `due_diligence` (DDA) and `political_analysis` (PAA). |
| v10     | May 2026   | Initial 10-agent foundation (Deep Research, CodeForge, VisualCraft, Narrative Weaver, Quant Analyst, Automation Orchestrator, Brazilian Cultural, Chief of Staff, Geopolitical Intelligence, News Monitor). |

---

## 📄 License

Personal and internal use. Feel free to adapt these agents for your own Grok workflows.

---

**Maintained by Alexandre Ataide**  
For questions, suggestions, or custom agent development, open an issue or reach out directly.

---

*Built with ❤️ for high-quality, production-ready AI agent work in Grok.*