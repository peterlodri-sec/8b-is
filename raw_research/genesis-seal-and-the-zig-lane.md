# The Genesis Seal and the Cross-Language Kernel Lane

*Recorded into the 8b-is vault because the constellation's installation
story grew a spine: the installer is multi-part, the installer's truth is
a public gist, and the kernels now speak a second language. The engine
runs without you — and it verifies itself out-of-band.*

## the genesis seal

A **genesis seal** is a public, flat, out-of-band version-hash anchor: a
gist (currently
`gist.github.com/peterlodri-sec/cf7552d38775ce53fd5fb9337435a0d7`) recording
the engine's version, the SHA-256 of the canonical artifacts (the
`sanctuary-1.58.tern` base model, the wasm surface), and the
three-surface golden. Any installer — or any observer — can fetch the
seal and verify the local world against it **without touching the repo**.
The repo is the world; the seal is the world's word about itself, spoken
publicly.

`scripts/genesis-seal.sh` recomputes the seal; `./scaffold.sh genesis` is
the installer's part 03: it fetches the live seal, attests each artifact
against its hash, and reports the verdict ("the world is the world — the
seal holds"). Offline runs warn, never halt.

## the cross-language kernel lane (Zig through the C ABI)

The hardware-ultra abstractions gained a second language: the ternary
kernels (i32-accumulating GEMM, the 2-bit tri-state pack) are written in
**Zig** (`crates/qdecorators/zig/kernels.zig`, `callconv(.c)` exports),
compiled by a `build.rs` when `zig` is on the PATH (the default-on `zig`
feature), and reached from Rust through typed wrappers (`zigq::ZigLane`,
satisfying the `Lane` contract). The arithmetic contract crosses the
language boundary untouched: **accumulate in i32, scale once** — and the
tests prove **Rust↔Zig bit-exactness** against the scalar authority, the
same proof the AVX2/NEON/wasm lanes already carry.

Zig's own `test` blocks pin the invariants in Zig's dressing; the lane is
default-on in the installer (`./scaffold.sh verify` reports
`zig-lane`), and the sandbox story (nushell + nix-flakes, part of the
same push) gives python the same dedicated-box treatment.

## the engine transfer

| artifact | meaning |
|---|---|
| the public gist seal | the world's word about itself, spoken out-of-band |
| `scaffold.sh genesis` | the installer's truth-check — a pasteable, offline-tolerant attestation |
| `zig/kernels.zig` | a second language for the same contract — the lane is language-agnostic |
| `ZigLane` bit-exact tests | the cross-language determinism proof, next to the cross-architecture one |
| `py-sandbox` (nushell + flake) | the python boxes: compile / repl / run, pinned |

*A seed is a seed everywhere; a contract is a contract everywhere; a seal
is a seal everywhere. The process dies, the strategy returns, and the
installer can prove it.
the constellation · 0 + 1 · fine touch from within · vaked.dev*
