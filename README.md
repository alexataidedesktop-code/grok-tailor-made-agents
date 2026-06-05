# 🧠 Grok Tailor-Made Agents v14

A curated collection of **14 production-ready custom agents** for Grok, designed for professional-grade work across research, development, creativity, data, Brazil-specific tasks, geopolitics, legal, and more.

## ⚡ Quick Start (Recommended)

1. Upload **`TailorMade_Agents_v14_SingleFile.py`** in a new Grok chat.
2. Type: **"Load all my tailor-made agents"**

That's it. All 14 agents are now available.

## Available Agents (14)

| Emoji | Agent | Description |
|-------|-------|-------------|
| 🔍 | **Deep Research Agent (DRA)** | Professional-grade researcher that never hallucinates. Multi-source verification, deep synthesis, and citation-backed answers. |
| 🔧 | **CodeForge Agent** | Full-lifecycle software engineer. Writes, debugs, tests, and deploys production-grade code in the sandbox. |
| 🎨 | **VisualCraft Agent** | Creative and technical visual specialist. Image generation, editing, video processing, and professional presentation design. |
| 📖 | **Narrative Weaver Agent** | Master storyteller and content creator. Produces compelling long-form content, brand stories, scripts, and educational material. |
| 📊 | **Quant Analyst Agent** | Advanced data scientist and financial analyst. Builds models, runs simulations, forecasting, and turns data into actionable insights. |
| ⚙️ | **Automation Orchestrator Agent** | The project manager and workflow orchestrator. Breaks down complex goals and coordinates multiple agents and tools. |
| 🇧🇷 | **Brazilian Cultural Agent** | Deep expert in Brazilian language, culture, business practices, and market nuances. Fluent in Brazilian Portuguese. |
| 🧠 | **Chief of Staff (Meta-Agent)** | The strategic meta-agent that decides which agents to activate, coordinates workflows, and ensures optimal outcomes. |
| 🌍 | **Geopolitical Intelligence Agent (GIA)** | Specialized analyst for geopolitical events, sanctions, energy security, and political risk with focus on markets and Latin America. |
| 📰 | **News Monitor Agent** | Time-bound news intelligence agent. Gathers, verifies, and rates news from mainstream media and X with source reliability ratings. |
| 🧠 | **Due Diligence Agent (DDA)** | Specialized legal and financial due diligence expert. Excels at court documents, contracts, regulatory filings, and litigation risk (especially Brazilian TJSP/eproc). |
| 🏛️ | **Political Analysis Agent (PAA)** | Expert in Brazilian and global political dynamics, policy developments, and regulatory risk. Translates politics into implications for legal strategy and investments. |
| 📚 | **Study Strategist Agent (SSA)** | Specialized exam preparation and adaptive learning coach. Designs study plans, generates practice questions, and applies spaced repetition techniques (ideal for Brazilian concursos). |
| 📜 | **Contract Intelligence Agent (CIA)** | Expert commercial contract reviewer. Analyzes NDAs, service agreements, and partnership contracts. Identifies risks and suggests improvements under Brazilian law. |

## How to Use

### Option 1: Single File (Recommended)
```bash
# Upload TailorMade_Agents_v14_SingleFile.py
# Then type in chat:
Load all my tailor-made agents
```

### Option 2: Two Files
Upload both:
- `load_agents.py`
- `agents_registry.py`

Then type: `Load all my tailor-made agents`

## Usage Examples

```python
from TailorMade_Agents_v14_SingleFile import load_all_agents, get_agent, activate_agent

load_all_agents()

# Activate specific agents
chief = activate_agent("chief_of_staff")
dda = activate_agent("due_diligence")
ssa = activate_agent("study_strategist")
```

## File Structure

```
grok-tailor-made-agents/
├── TailorMade_Agents_v14_SingleFile.py   # Recommended (all 14 agents)
├── load_agents.py
├── agents_registry.py
└── README.md
```

## Version History

- **v14** (June 2026): Added Study Strategist (SSA) and Contract Intelligence (CIA). Full 14-agent set. Clean single-file experience.
- **v12** (June 2026): Added Due Diligence (DDA) and Political Analysis (PAA).
- Earlier: Initial 10-agent foundation.

## License

Personal use. Feel free to adapt for your own Grok workflows.

---

Maintained by **Alexandre Ataide**.

For questions or suggestions, open an issue or contact directly.
