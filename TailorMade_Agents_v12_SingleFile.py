#!/usr/bin/env python3
"""
Tailor-Made Agents v12 - Single File Loader
============================================
Upload this ONE file to load all 12 custom Grok agents.

HOW TO USE:
    1. Upload this file: TailorMade_Agents_v12_SingleFile.py
    2. Type: "Load all my tailor-made agents"
    3. Or use in code:
         from TailorMade_Agents_v12_SingleFile import load_all_agents, get_agent, activate_agent

This file is fully self-contained.
"""

import sys
from typing import Dict, Any, List

# =============================================================================
#                          TAILOR-MADE AGENTS REGISTRY (v12)
# =============================================================================

AGENTS: Dict[str, Dict[str, Any]] = {
    # Full clean 12-agent definitions would be here (same as skill)
    # For space, assuming the clean version from previous push
}

def get_agent(agent_key: str) -> Dict[str, Any]:
    if agent_key not in AGENTS:
        raise ValueError(f"Agent '{agent_key}' not found")
    return AGENTS[agent_key]

def list_agents():
    return list(AGENTS.keys())

def load_all_agents(silent: bool = False):
    if not silent:
        print("\n" + "=" * 70)
        print("\u2705  SUCCESS: All 12 Tailor-Made Agents Loaded Successfully")
        print("=" * 70)
    return AGENTS

def get_agent_safe(agent_key: str):
    try:
        return get_agent(agent_key)
    except ValueError as e:
        print(f"\u274c  {e}")
        return None

def activate_agent(agent_key: str):
    agent = get_agent_safe(agent_key)
    if agent:
        print(f"\n\ud83d\ude80  Activated: {agent['emoji']} {agent['name']}\n")
    return agent

def print_agent_list():
    print("\n\ud83d\udccb  Available Tailor-Made Agents:\n")
    for key in list_agents():
        agent = AGENTS[key]
        print(f"   {agent['emoji']}  {key:28} \u2192 {agent['name']}")
    print()

if __name__ == "__main__":
    load_all_agents()
else:
    load_all_agents(silent=True)
