# Raw Research Contribution Guide

> **Welcome to the 8b-is Raw Research Vault.** This directory contains unrefined, work-in-progress, and peer-reviewed mathematical proofs, LaTeX equations, and research blueprints for **AXIOM QUANT**.

---

## 🗂 the recorded corpus (index)

- [the-8b-is-org-constellation.md](the-8b-is-org-constellation.md) — the org's repository map: the AGNOS stack (prakash, bhava, tanmatra, jantu, PhoenixiX, cinematic-reconstruction, rustybox, smart-tree, bodh, goonj, libro), the theory repos (spherepop, mem8*), the engine surfaces — navigation for every session
- [son-go-ku-training-concept.md](son-go-ku-training-concept.md)
- [the-illustrated-man-surfaces-wear-the-stories.md]
- [graph-and-network-theory-foundations.md]
- [mem8-hypermesh-quad.md]
- [obliterated-lane.md](obliterated-lane.md) — the top-4 abliterated models through unsloth → MLX + GGUF: the world-dataset fine-tune, the mirror's 10 GB gates, the colab-mcp proxy flow(mem8-hypermesh-quad.md) — the 8-byte MEMNET memory cell: bilinear phase addressing, observer-relative origo, boolean gates, the i32 overflow proof — and the Zig twin, bit-exact(graph-and-network-theory-foundations.md) — Benjamin (2025) + Estrada (Strathclyde): the field absorbed — ER graphs, centrality, communities, communicability, consensus, epidemics — with the full engine-transfer table (UltraGraph speaks its language)
- [school-topography-blueprint.md]
- [assembly-plan-a-e.md](assembly-plan-a-e.md) — the found assembly plan as the constellation's zones: Great Hall C = the hub, the D rooms = instances, the spiral = the ring, the sandbox = every seed's playground(school-topography-blueprint.md) — METSZET-style ASCII blueprint: the school as a zone — site plan with contours, section A-A through the storeys, the title block ("metszet = az igazság vágása")(the-illustrated-man-surfaces-wear-the-stories.md) — Bradbury: the floors are the world's tattoos — a tattoo does not narrate, it IS; plus the ez-ffmpeg media-lane reference
- [genesis-seal-and-the-zig-lane.md](genesis-seal-and-the-zig-lane.md) — the constellation installs with a spine: the public genesis-seal gist, the multi-part installer, and the Zig kernels (cross-language bit-exact) — Goku Gets Married! (ch. 171): the training concept — strength folds into the heart, the heart folds into the strength; the heart lane, the promise as `commit`, "a promise is a promise"
- [music-let-the-light-in.md](music-let-the-light-in.md) — Jen Hartsfield, "Let The Light In" — prakash's hymn: light as the AGNOS stack's first lane
- [music-the-operating-system-that-must-sleep.md](music-the-operating-system-that-must-sleep.md) — constellation music: a 30-minute piece whose title is the engine's doctrine in audio — the world runs without you; your OS must sleep
- [notes-of-the-spoon.md](notes-of-the-spoon.md) — Osahon Ize-Iyamu, "Tenger az aszfalt helyen": the spoon as the note theory's simplest proof — generative + capture, the engine's four operators in one object
- [spherepop-toward-a-complete-theory.md](spherepop-toward-a-complete-theory.md) — Flyxion: the complete theory of histories-first computation — the four operators (Pop/Refuse/Bind/Collapse), the note taxonomy, VIEW vs COLLAPSE, GC as collapse, the L2 state illusion — the engine's operator set formalized
- [hub-instance-mmo-architecture.md](hub-instance-mmo-architecture.md) — the Gemini planning session, synthesized: hub-and-instance world split, the Tokio event loop, shared-crate superpower — with the adoption/rejection table against the engine's own decisions
- [commitment-before-appearance.md](commitment-before-appearance.md) — Flyxion: one log, two folds (material M + semantic S), attestation boundary, jurisdictional drift — the engine's architecture formalized
- [motion-before-mechanism.md](motion-before-mechanism.md) — Flyxion: robust moments as lossy witnesses; reliability vs identifiability, the structural fiber, named regions over a many-to-one preimage
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
