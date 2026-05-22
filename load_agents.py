#!/usr/bin/env python3
"""
Tailor-Made Agents Loader
=========================
Easy way to load and use your 10 custom Grok agents.

Usage in Grok chats:
    1. Upload this file + agents_registry.py
    2. Type: "Load all my tailor-made agents"
    3. Or run: from load_agents import load_all_agents

Usage locally:
    python load_agents.py
"""

import sys
from pathlib import Path

# Make sure we can find agents_registry.py in the same folder
sys.path.insert(0, str(Path(__file__).parent))

from agents_registry import AGENTS, get_agent, list_agents


def load_all_agents(silent: bool = False) -> dict:
    """
    Load all 10 tailor-made agents.
    Returns the AGENTS dictionary.
    Set silent=True to load without printing.
    """
    if not silent:
        print("\n" + "="*60)
        print("✅ SUCCESS: All 10 Tailor-Made Agents Loaded")
        print("="*60)
        print(f"Total agents: {len(AGENTS)}")
        print("-"*60)
        
        for key in list_agents():
            agent = AGENTS[key]
            print(f"  {agent['emoji']} {agent['name']}")
        
        print("-"*60)
        print("Ready to use. Example:")
        print("   dra = get_agent('deep_research')")
        print("="*60 + "\n")
    
    return AGENTS


def print_agent_list():
    """Pretty print all available agents with emojis."""
    print("\n📋 Available Tailor-Made Agents:\n")
    for key in list_agents():
        agent = AGENTS[key]
        print(f"  {agent['emoji']} {key:25} → {agent['name']}")
    print()


def get_agent_safe(agent_key: str):
    """Safe version of get_agent with helpful error message."""
    try:
        return get_agent(agent_key)
    except ValueError as e:
        print(f"❌ {e}")
        print("Available keys:", list_agents())
        return None


if __name__ == "__main__":
    # When run directly, load and show everything nicely
    load_all_agents()
    print("\nYou can now use any agent with:")
    print("    from load_agents import get_agent")
    print("    agent = get_agent('deep_research')  # or any other key\n")
