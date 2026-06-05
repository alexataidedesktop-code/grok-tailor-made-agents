#!/usr/bin/env python3
"""
Tailor-Made Agents Loader v14
=============================
Easy way to load and use your 14 custom Grok agents.

Usage in Grok chats:
    1. Upload this file + agents_registry.py
    2. Type: "Load all my tailor-made agents"
    3. Or run: from load_agents import load_all_agents

Usage locally:
    python load_agents.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from agents_registry import AGENTS, get_agent, list_agents


def load_all_agents(silent: bool = False) -> dict:
    """
    Load all 14 tailor-made agents.
    Returns the AGENTS dictionary.
    Set silent=True to load without printing.
    """
    if not silent:
        print("\n" + "="*60)
        print("\u2705 SUCCESS: All 14 Tailor-Made Agents Loaded")
        print("="*60)
        print(f"Total agents: {len(AGENTS)}")
        print("-"*60)
        
        for key in list_agents():
            agent = AGENTS[key]
            print(f"  {agent['emoji']} {agent['name']}")
        
        print("-"*60)
        print("Ready to use. Example:")
        print("   dra = get_agent('deep_research')")
        print("   dda = get_agent('due_diligence')")
        print("   paa = get_agent('political_analysis')")
        print("   ssa = get_agent('study_strategist')   # New: Exam prep & study planning")
        print("   cia = get_agent('contract_intelligence')  # New: Contract review & risk analysis")
        print("   chief = get_agent('chief_of_staff')")
        print("="*60 + "\n")
    
    return AGENTS


def print_agent_list():
    """Pretty print all available agents with emojis."""
    print("\n\ud83d\udccb Available Tailor-Made Agents (14):\n")
    for key in list_agents():
        agent = AGENTS[key]
        print(f"  {agent['emoji']} {key:25} \u2192 {agent['name']}")
    print()


def get_agent_safe(agent_key: str):
    try:
        return get_agent(agent_key)
    except ValueError as e:
        print(f"\u274c {e}")
        print("Available keys:", list_agents())
        return None


if __name__ == "__main__":
    load_all_agents()
    print("\nYou can now use any agent with:")
    print("    from load_agents import get_agent")
    print("    agent = get_agent('deep_research')  # or any other key\n")
