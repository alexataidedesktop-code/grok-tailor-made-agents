#!/usr/bin/env python3
"""
Test script for Tailor-Made Agents Registry v14
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from agents_registry import AGENTS, get_agent, list_agents


def main():
    print("=" * 70)
    print("TAILOR-MADE AGENTS v14 - VALIDATION TEST")
    print("=" * 70)

    assert len(AGENTS) == 14, f"Expected 14 agents, got {len(AGENTS)}"
    print(f"✅ Registry has {len(AGENTS)} agents")

    # Test a few key agents
    for key in ["deep_research", "chief_of_staff", "due_diligence", "study_strategist", "contract_intelligence"]:
        agent = get_agent(key)
        assert "system_prompt" in agent and len(agent["system_prompt"]) > 100
        print(f"✅ {agent['emoji']} {agent['name']}")

    print("\n🎉 ALL TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
