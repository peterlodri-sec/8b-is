# Raw Research Contribution Guide

> **Welcome to the 8b-is Raw Research Vault.** This directory contains unrefined, work-in-progress, and peer-reviewed mathematical proofs, LaTeX equations, and research blueprints for **AXIOM QUANT**.

---

## 🗂 the recorded corpus (index)

- [inscription-before-collusion.md](inscription-before-collusion.md) — Flyxion: external memory, distributed recurrence, and the appearance of agent swarms (the wiki incident, the evidentiary ladder, constraint laundering, population memory)
- [layers-of-a-persistent-world.md](layers-of-a-persistent-world.md) — Flyxion: the four layers (rendering / M / Q / H) of a persistent world + the observer's architecture
- [inscription-before-rendering.md](inscription-before-rendering.md) — Flyxion: custody, recurrence, and the missing conditions of preservation
- [research-clusters-quantum-worldmodels.md](research-clusters-quantum-worldmodels.md) — the parallel cluster reports A–F: quantum geometry + world models
- [mind-games-intuitive-physics.md](mind-games-intuitive-physics.md) — intuitive physics as a game-design lever
- [indie-fund-application.md](indie-fund-application.md) — the Indie Fund application (cabotage@pm.me, vaked.dev)
- [rsvp-lineage-2021-precursor.md](rsvp-lineage-2021-precursor.md) — the 2021 rsvp lineage precursor
- [every-observer-at-the-vertex.md](every-observer-at-the-vertex.md) — observers at the vertex
- [eos-cla-v1.md](eos-cla-v1.md) — the EOS-CLA v1.0
- [game-studio-vaked.md](game-studio-vaked.md) — the vaked game studio record

---

## 📝 How to Contribute

### Option A: Direct Git Contribution
1. Create a new Markdown file under `raw_research/`:
   ```bash
   raw_research/YYMMDD-topic-short-name.md
   ```
2. Format your paper using LaTeX delimiters (`$ ... $` for inline, `$$ ... $$` for display blocks).
3. Include metadata headers:
   ```markdown
   # Paper Title
   **Author:** Standard Galactic (@standardgalactic) / P. Lodri (@peterlodri-sec)
   **Date:** YYYY-MM-DD
   **Tags:** #graph-theory #quantum-calculus #bitnet #loop-engineering
   ```
4. Commit and push to `main` or submit a Pull Request.

---

## 🤖 Option B: Via MCP Server (`raw_research_mcp`)

AI agents can submit raw research programmatically using the `raw_research_mcp` server:

```python
# MCP Tool Invocation
submit_raw_research(
    title="Zeta Zero Spacing & GUE Level Repulsion",
    author="Standard Galactic",
    content="Raw LaTeX notes on Montgomery pair correlation...",
    tags=["zeta-zeros", "gue", "sine-kernel"]
)
```

---

## 📐 Template Format (`raw_research/paper_template.md`)

```markdown
# [Title of Research Paper]

**Author:** [Your Name / Alias]  
**Date:** [YYYY-MM-DD]  
**Tags:** #tag1 #tag2 #tag3  

## 1. Abstract
Brief summary of the mathematical proof or experimental conjecture.

## 2. Mathematical Formulation
$$\mathcal{L} \psi = \lambda \psi$$

## 3. Empirical Verification
- Code snippets / python scripts.
- Benchmark data tables.
```
