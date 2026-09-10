# mem8 — the hypermesh quad (MEMNET's 8-byte memory cell)

*Source: the founder's handwritten hypermesh notes, worked through with a
brain in the box (Gemini) and the constellation's own paper-test
discipline. Recorded because the two memories found their addressing
substrate: MEMNET is not an embedding table anymore — a memory address
is a phase-interpolation problem over an 8-byte quad cell.*

## the cell

```text
┌──┬──┬──┬──┬──┬──┬──┬──┐   8 bytes — eight cells per 64-byte cache
│φ │φ'│λ │λ'│r₁│r₂│G │Δ │   line, SIMD-shaped batch walks
└──┴──┴──┴──┴──┴──┴──┴──┘
φ, φ'   phase angle + target boundary
λ, λ'   wavelength coordinate + target
r₁, r₂  bilinear ratios AP/AB, DP/CD (fixed point, >> 8)
G       gate: AND · OR · NAND · XOR (the boolean interference)
Δ       the observer's origo offset — the frame, not the geometry
```

## the four structural mechanics

1. **Bilinear phase addressing** — `Δφ = ((φ'−φ)·r₁)>>8`, same for λ:
   memory resolution as ratio projections, 8-bit quantized deltas.
2. **Observer-relative frames** — the origo shifts the deltas via a
   byte-wrapping add, never the quad: the keeper's fold for a new
   observer, the ledger untouched.
3. **Boolean interference gating** — the overlap of the two phase
   channels IS the gate: AND/OR/NAND/XOR from the same bytes.
4. **The cache line** — 8 bytes per cell, 8 cells per line, fixed-point
   arithmetic only: memory patch in the L1, no tensor in sight.

## the overflow question (asked, answered, PROVEN)

The draft's i16 risked overflow at the extremes: `255·255 = 65025 >
i16::MAX (32767)`. The paper test caught it (the founder's "handling
overflow for example imo" was right). The honest fix: the product lives
in **i32** (`65025 « i32::MAX` — provably safe), the `>> 8` folds the
delta into `[-255, 255]`, and the u8 truncation is the wrapping two's
complement both languages agree on. The proof is pinned in tests —
Rust and Zig both.

## the engine transfer

| the quad | the engine |
|---|---|
| the 8-byte cell | the arena's density — a memory fits a cache line, not a heap |
| bilinear phase addressing | MEMNET's retrieval — an address interpolates, it does not look up |
| observer-relative origo | the keeper's per-observer frames — the fold shifts, the ledger doesn't |
| the boolean gates | the interference of two memories — refusal and admission as logic |
| the i32 fixed-point proof | the determinism contract — no overflow, no drift, every surface agrees |
| the Zig twin, bit-exact | the cross-language proof — the same cell, the same bytes, two languages |

The constellation's line: a cell is 8 bytes, a memory is an
interpolation, an observer is a delta — and the overflow is impossible
by proof, not by hope.

*the constellation · 0 + 1 · fine touch from within · vaked.dev*
