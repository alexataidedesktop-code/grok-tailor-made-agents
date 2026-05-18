#!/usr/bin/env python3
"""
Convenient loader for all Tailor-Made Agents
Makes it super easy to use the agents locally.

Usage examples:
    from load_agents import load_all_agents, get_agent

    agents = load_all_agents()
    dra = get_agent("deep_research")
"""

import sys
from pathlib import Path

# Add current folder to Python path so it can find agents_registry.py
sys.path.insert(0, str(Path(__file__).parent))

from agents_registry import AGENTS, get_agent, list_agents, print_agent_summary


def load_all_agents():
    """Load and return all agents with a nice message."""
    print(f"✅ Loaded {len(AGENTS)} tailor-made agents successfully!\n")
    return AGENTS


if __name__ == "__main__":
    # When you run this file directly, it shows all agents
    agents = load_all_agents()
    
    print("Available agents:")
    for key in list_agents():
        agent = agents[key]
        print(f"  {agent['emoji']} {key}: {agent['name']}")
    
    print("\nExample usage:")
    print("  from load_agents import get_agent")
    print("  agent = get_agent('deep_research')")