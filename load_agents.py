#!/usr/bin/env python3
"""
Tailor-Made Agents Loader v14
=============================
Easy loader for all 14 custom Grok agents.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from agents_registry import AGENTS, get_agent, list_agents


def load_all_agents(silent: bool = False):
    if not silent:
        print("\n" + "="*70)
        print("✅ SUCCESS: All 14 Tailor-Made Agents Loaded")
        print("="*70)
        print(f"Total agents: {len(AGENTS)}")
        print("-"*70)
        for key in list_agents():
            agent = AGENTS[key]
            print(f"  {agent['emoji']} {agent['name']}")
        print("-"*70)
        print("Example: dra = get_agent('deep_research')")
        print("="*70 + "\n")
    return AGENTS


def get_agent_safe(agent_key: str):
    try:
        return get_agent(agent_key)
    except ValueError as e:
        print(f"❌ {e}")
        return None


if __name__ == "__main__":
    load_all_agents()
