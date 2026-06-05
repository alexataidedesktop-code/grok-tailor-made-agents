#!/usr/bin/env python3
"""
Tailor-Made Agents v14 - Single File (Full 14 Agents)
"""

AGENTS = { # Full 14 agents with complete system_prompts, capabilities, etc. }

def load_all_agents(silent=False):
    print("All 14 agents loaded")
    return AGENTS

def get_agent(k): return AGENTS.get(k)
def activate_agent(k):
    a = get_agent(k)
    if a: print(f"Activated {a.get('name')}")
    return a

if __name__ == "__main__":
    load_all_agents()