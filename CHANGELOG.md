# Tailor-Made Agents Changelog

All notable changes to the Tailor-Made Agents Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Due Diligence Agent (DDA) 📋**
  - Specialized investment research agent for deep company-level fundamental analysis.
  - Focus on financial statement scrutiny, competitive moat assessment, management quality, red flags, and investment thesis construction (bull/base/bear cases).
  - Structured response with Valuation Considerations and Key Questions for Further Research.

- **Political Analysis Agent (PAA) 🏛️**
  - Expert in domestic political analysis with particular strength in Brazil and Latin America.
  - Surfaces local political experts while explicitly accounting for their biases.
  - Assesses power dynamics, legislative impact, electoral consequences, and scenario planning (Base / Upside / Downside).
  - Strong focus on implications for stability, reform, and who gains/loses power.

### Changed
- **Chief of Staff (Meta-Agent)**: Updated internal knowledge list to include all 12 agents (DDA + PAA).
- **Registry**: Now contains exactly 12 production-ready agents.
- `load_agents.py` and documentation updated for the expanded ecosystem.
- README table and descriptions refreshed.

### Validation
- Full syntax and structural validation passed.
- All 12 agents load correctly with required fields present.
- New agents follow the same high-quality prompt and capability standards as existing ones.

---

## Previous Versions

> Initial 8-agent registry created in April–May 2026.  
> GIA and News Monitor agents added in May 2026.
> Due Diligence (DDA) and Political Analysis (PAA) agents added in June 2026.

---

**Maintained by:** Alexandre Ataide  
**Last Updated:** June 03, 2026