#!/usr/bin/env python3
"""
Test script for Tailor-Made Agents Registry
Run this after cloning/pulling to validate everything works.
"""

import sys
from pathlib import Path

# Add current directory to path so we can import agents_registry
sys.path.insert(0, str(Path(__file__).parent))

from agents_registry import AGENTS, get_agent, list_agents


def test_registry_loads():
    """Test that the registry loads without errors."""
    print("🔍 Testing registry import and basic loading...")
    assert len(AGENTS) == 10, f"Expected 10 agents, got {len(AGENTS)}"
    print(f"   ✅ Registry loaded successfully with {len(AGENTS)} agents")
    return True


def test_all_agents_have_required_fields():
    """Verify every agent has the required structure."""
    print("\n🔍 Testing that all agents have required fields...")
    required = ['name', 'emoji', 'description', 'system_prompt', 'allowed_tools', 'capabilities', 'example_prompts']
    
    for key, agent in AGENTS.items():
        missing = [field for field in required if field not in agent]
        if missing:
            raise AssertionError(f"Agent '{key}' is missing fields: {missing}")
        print(f"   ✅ {agent['emoji']} {key}")
    print("   ✅ All agents have complete structure")
    return True


def test_get_agent_function():
    """Test the get_agent helper."""
    print("\n🔍 Testing get_agent() helper...")
    dra = get_agent('deep_research')
    assert dra['name'] == "Deep Research Agent (DRA)"
    print("   ✅ get_agent('deep_research') works correctly")

    # Test invalid key
    try:
        get_agent('nonexistent_agent')
        raise AssertionError("Should have raised ValueError for invalid key")
    except ValueError as e:
        print(f"   ✅ Correctly raises error for invalid agent: {e}")
    return True


def test_chief_of_staff_knowledge():
    """Ensure Chief of Staff knows about the new agents."""
    print("\n🔍 Testing Chief of Staff knowledge of all agents...")
    chief = get_agent('chief_of_staff')
    prompt = chief['system_prompt']
    
    assert "Geopolitical Intelligence" in prompt, "Chief of Staff missing GIA"
    assert "News Monitor" in prompt, "Chief of Staff missing News Monitor"
    print("   ✅ Chief of Staff correctly lists all 10 agents")
    return True


def test_new_agents_exist():
    """Specifically test the two newest agents."""
    print("\n🔍 Testing new agents (GIA + News Monitor)...")
    
    gia = get_agent('geopolitical_intelligence')
    assert "GIA" in gia['name']
    print(f"   ✅ {gia['emoji']} {gia['name']} loaded")

    news = get_agent('news_monitor')
    assert "News Monitor" in news['name']
    print(f"   ✅ {news['emoji']} {news['name']} loaded")
    return True


def main():
    print("=" * 60)
    print("🧪 TAILOR-MADE AGENTS REGISTRY - VALIDATION TEST")
    print("=" * 60)
    
    try:
        test_registry_loads()
        test_all_agents_have_required_fields()
        test_get_agent_function()
        test_chief_of_staff_knowledge()
        test_new_agents_exist()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED — Registry is healthy and ready!")
        print("=" * 60)
        print("\nYou can now safely use:")
        print("   from load_agents import load_all_agents, get_agent")
        print("   agents = load_all_agents()")
        return 0
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())