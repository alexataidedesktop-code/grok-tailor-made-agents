# Tailor-Made Agents Changelog

All notable changes to the Tailor-Made Agents Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Geopolitical Intelligence Agent (GIA) 🌍**
  - New specialized agent for geopolitical risk, sanctions, energy security, and political analysis.
  - Strong focus on translating developments into market, investment, and supply chain implications.
  - Includes structured scenario planning (Base / Bull / Bear cases) and LatAm/Brazil relevance.
  - Response format: Event Summary → Market Implications → Risk Scenarios → Monitoring Dashboard → Source Assessment.

- **News Monitor Agent 📰**
  - Time-bound news intelligence agent with strict horizon enforcement (default: last 24 hours).
  - Advanced source strategy including mainstream, X/Twitter, regional/local publications (including non-English), and specialized sources.
  - Mandatory direct source links for every development.
  - Reliability ratings (High / Medium-High / Medium / Low-Medium).
  - Improved organization: supports subtopic grouping and expanded "Full Sources" categorized section.
  - Enhanced rules for local/regional coverage and non-English sources.

### Changed
- **Chief of Staff (Meta-Agent)**: Updated internal knowledge list to include all 10 agents (GIA + News Monitor).
- **Registry**: Now contains exactly 10 production-ready agents.
- Minor prompt refinements across agents for consistency and clarity.

### Validation
- Full syntax and structural validation passed.
- All 10 agents load correctly with required fields present.
- `load_agents.py` and helper functions updated for 10-agent ecosystem.

---

## Previous Versions

> Initial 8-agent registry created in April–May 2026.  
> GIA and News Monitor agents added in May 2026.

---

**Maintained by:** Alexandre Ataide  
**Last Updated:** May 22, 2026