# Grok Tailor-Made Agents

A collection of **10 powerful, ready-to-use AI agents** designed to extend Grok's capabilities across research, development, creativity, finance, orchestration, and specialized domains.

## Available Agents

| Agent                              | Emoji | Purpose |
|------------------------------------|-------|---------|
| Deep Research Agent (DRA)          | 🔍    | Professional-grade research, multi-source verification & fact-checking |
| CodeForge Agent                    | 🛠️    | Full-lifecycle software engineering, debugging & deployment |
| VisualCraft Agent                  | 🎨    | Image & video generation/editing, presentations & visual design |
| Narrative Weaver Agent             | 📖    | Storytelling, long-form content, brand narratives & copywriting |
| Quant Analyst Agent                | 📊    | Data science, financial modeling, forecasting & statistical analysis |
| Automation Orchestrator Agent      | ⚙️    | Complex project breakdown, multi-agent orchestration & workflow automation |
| Portuguese-Brazilian Cultural Agent| 🇧🇷    | Brazilian culture, Portuguese localization, business practices & market insights |
| Chief of Staff (Meta-Agent)        | 🧠    | Strategic meta-orchestration, agent coordination & high-level planning |
| Geopolitical Intelligence Agent (GIA) | 🌍 | Geopolitical risk, sanctions, energy security, political analysis & scenario planning |
| News Monitor Agent                 | 📰    | Time-bound news intelligence, source reliability ratings & real-time monitoring |

## Quick Start (Local)

```bash
git clone https://github.com/YOUR_USERNAME/grok-tailor-made-agents.git
cd grok-tailor-made-agents
python load_agents.py
```

## Usage Example

```python
from load_agents import load_all_agents, get_agent

agents = load_all_agents()
print(f"Loaded {len(agents)} agents successfully!\n")

# Activate any agent
dra = get_agent("deep_research")
print(dra["name"], dra["emoji"])
```

## Repository Structure

- `agents_registry.py` — Full agent definitions with system prompts, capabilities & tools
- `load_agents.py` — Convenient loader for all agents
- `README.md` — This file
- `LICENSE` — MIT License

---

**Maintained with ❤️ for the Grok ecosystem**  
All agents are production-ready and follow consistent high-quality standards.
