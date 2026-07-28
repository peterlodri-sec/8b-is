# Raw Research Contribution Guide

> **Welcome to the 8b-is Raw Research Vault.** This directory contains unrefined, work-in-progress, and peer-reviewed mathematical proofs, LaTeX equations, and research blueprints for **AXIOM QUANT**.

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
