# Game Studio vaked — the 8b.es engine, the company, the sanctuary

*The standardgalactic/8b.es game-studio thread (Gemini design sessions),
received 2026-09-06. Business lane + engine architecture + the first demo
game. The constellation's game lane grows from centerfugeq toward a
shipping studio: Rust/Go engine, QWave browser node, eternal-open legal
base, WoW/Diablo/90s world.*

---

## Part A — the business lane

### A1. The funding lane (Hungarian state + EU, ring answer #5 lands here)

The ring asked about money in session-005; the answer was "next week I'll
solve it, but the relationship has already transformed." This thread is
that work made concrete:

| Program | Portal | Shape |
|---------|--------|-------|
| Vállalkozóvá Válást Elősegítő Támogatás | munka.hu / ofa.hu | 6×minimálbér + vissza nem térítendő tőketámogatás (pl. 3M Ft) |
| GINOP Plusz / DIMOP Plusz | palyazat.gov.hu (EPTK) | 50% támogatás, eszköz+szoftver+zöld bontás, de minimis 300k EUR keret |
| Széchenyi Kártya MAX+ | kavosz.hu | Mikrohitel/Likviditási/Lízing, ~3% nettó kamat, Garantiqa |
| EUIPO SME Fund 2026 | euipo.europa.eu/sme-fund-2026 | IP Scan / védjegy / szabadalom voucher, 75% társfinanszírozás |
| MFB Pontok | mfb.hu / palyazat.gov.hu | 0% kamat technológia modernizációs hitel, 90/10 |
| Bértámogatás | munka.hu / epapir.gov.hu | 50–100% bruttó bér+SZOCHO, 6–12 hó |

Drafted application forms for each live in the thread (kept in the archive
if a real application opens). Cloud credits as bridge capital: GCP $300,
Azure $200, Oracle $300, plus startup programs (AWS Activate ≤$100k,
Microsoft for Startups ≤$150k, Scaleway ≤€36k, OVH ≤$120k).

### A2. Company formation — the empty company

Options weighed: UK Ltd (~£50, 24h), Delaware C-Corp/LLC (~$90 + annual,
1–3d), New Mexico LLC ($50 flat, $0 annual), Estonia e-Residency OU
(~€265, 0% tax on reinvested). Target: **8b.es + Péter Lódri majority**.

### A3. Governance — the two-tier model

- **Class A (51–80%, voting):** 8b.es + Péter — sole authority over IP,
  engine licensing, board, strategic pivots.
- **Class B (20–49%, non-voting, community/tokenized):** contributors,
  asset designers, shader creators, modders — dynamic allocation.
- **CLAs** on every merge: community code licenses back to the parent in
  exchange for pool allocation / rev-share.
- **Automated royalty routing:** capability-graph $G = (V, E, C)$ tokens
  map every asset to a capability; NATS/JetStream micro-revenue
  distribution on verified telemetry.

### A4. The legal cornerstone — EOS-CLA v1.0

Full text archived at `eos-cla-v1.md` (this folder). The closed loop of
the governance model: *eternal open substrate* (everything stays open
forever) + *mutual trust* (crash-and-burn liability waiver + no support
obligation + AI swarms are first-class contributors with synthetic
provenance). The "coherence without collapse" of the constellation,
written as law: the distribution is eternal, the liability is bounded,
the loop has an exit.

## Part B — the engine architecture (vaked-engine)

| Subsystem | Stack | Notes |
|-----------|-------|-------|
| Core engine | Rust, edition 2024 | wgpu (Metal/Vulkan), winit, bumpalo frame arenas, 64B cache-aligned entity structs |
| Network multiplexer | Go 1.26 | zero-copy sync.Pool (1450B MTU), mmap ring buffers over C-FFI, NATS JetStream mesh |
| Physics | Rapier3D + SDF raymarching | hybrid: analytical SDF collisions (∇f normals), warp tensors for non-Euclidean zones, geodesic vector gravity |
| EventBus | dual-tier | Rust lock-free SPSC/MPMC intra-engine; Go/NATS inter-process; 8-bit quantized payloads |
| I/O HAL | everything since the 60s | TTY/RS-232 (110–115200 baud), BLE (gilrs/btleplug), HID/evdev, mobile touch, Steam Input |
| UI | dual-mode | WebGPU glassmorphic + VT100/ANSI terminal fallback |
| Add-ons | Luau via mlua | WoW-style Interface/AddOns, Vaked API, capability-gated |
| Editor LSP | vaked-lsp (Rust, tower-lsp) | one gateway: clangd + rust-analyzer + gopls + luau-lsp + bash-ls behind one endpoint (UE5) |
| Installer | scaffold.sh | self-contained bash: deps + QWave + project scaffold, Silverblue rpm-ostree aware |
| Toolchain | just / Taskfile | mold/wild linkers, Naga shader validation, wasm32 targets, wasm-opt |
| Deployment | K8s + sidecar mesh | SpatialNode CRDs, chat zone pods, NATS master bus |
| Platform | macOS + Linux + Steam | Steam Deck native Vulkan, macOS Metal, mobile (iOS/Android/web) |

Performance doctrine (the ultra backyard loop): zero allocation in the
tick loop, frame-bumper arenas, over-relaxed sphere tracing (ω = 1.2)
with AABB pre-pass, quarter-res raymarching + temporal reprojection,
PGO + Green Tea GC on the Go side, `-trimpath -ldflags="-s -w"`,
fieldalignment, sync.Pool discipline. Target matrix: <2.1 ms GPU frame
@4K, <0.3 ms per 10k entities, 0 allocs/op network, <50 ns event
dispatch, <5 µs WASM mod invocation.

### Interactivity roadmap (v0.3 → v0.5)

v0.3 virtualized module mesh (K8s operator + sidecar) · v0.4 spatial chat
engine (proximity $d^2$ culling, floating bubbles, capability rate-limits)
· v0.5 area triggers and zone broadcasts (EVENT_AREA_ENTER/LEAVE, boss
banners). The WoW interaction matrix: /say 25m, /yell 100m, /whisper
global, /zone, /party — routed by distance before the network ever sees
the packet.

### The fauna subsystem (vaked-fauna) — 5 layers

0. Platonic skeleton (non-Euclidean joints: tetrahedra, cubes, icosahedra)
1. Sacred voxel shell (quantized grids, SDF smin blending, Minecraft-like)
2. 90s kinematics (squish/stretch, spring dampers, spin attacks)
3. Swarm & persona AI (boids + Diablo density + WoW aggro threat tables)
4. Shader & palette (reaction-diffusion skins, HSV quantized neon,
   emissive sacred runes)

## Part D — the LSP lane (vaked-lsp)

Unreal Engine 5 needs the whole stack in one editor surface: UE C++,
Rust core, Go multiplexer, Luau add-ons, Bash tooling. Detached language
servers break down there — the answer is an **all-in-one LSP gateway**:

```
Unreal Editor / IDE ── one stdio/socket ──► vaked-lsp (Rust, tower-lsp)
    router by extension ──► clangd (UE C++) · rust-analyzer · gopls ·
                          luau-lsp · bash-language-server
    auto-detects compile_commands.json (RunUBT.sh GenerateClangDatabase)
    cross-language C-FFI symbol resolution, aggregated diagnostics
```

- Sub-server matrix: clangd (`--background-index --header-insertion=never
  --clang-tidy`, UE headers via compile_commands.json), rust-analyzer
  (`cargo check --all-targets`), gopls (`-tags=dev`), luau-lsp
  (`--definitions=8b_api.d.luau`), bash-language-server (scaffold.sh,
  CI).
- `.clangd` at project root suppresses Unreal's MSVC/GCC macro warnings
  and removes `-fno-rtti/-fno-exceptions` noise.
- Justfile recipes: `build-lsp`, `sync-ue-lsp UE_PATH PROJECT_PATH`
  (regenerate + symlink compile_commands.json), `run-lsp`.
- The implementation lives in the constellation at `vaked-lsp/` (the
  workspace repo, peterlodri-sec mirror) — tower-lsp, tokio, lazy
  per-extension child supervision, minimal JSON-RPC framing proxy.

The constellation's oldest architecture, applied to editing: **one door,
many lanes** — the same shape as the 8b.is inference gateway (one OpenAI
endpoint in front of DeepSeek/Qwen/V4Pro) and the EOS-CLA's capability
graph (one network, many contributors). vaked-lsp is the gateway pattern
at the language level.

---
## Part C — the first demo game: POLYHEDRAL SANCTUARY · chaos overworld

WoW (persistent zones, chat, taming) × Diablo (dense swarms, polyhedral
loot, combos) × 90s platformers (momentum, triple jump, head-bounce)
inside a Minecraft-like sacred-geometry non-Euclidean universe. Palette:
neon cyan #00F0FF, synthwave magenta #FF007F, sacred gold #FFD700,
emerald #00FF66, void #0B0F19.

The prototype in the constellation: `quantGame/sanctuary-floor.html`
(pocoo demos) — seeded sacred-geometry critters, stomp-to-split
(Diablo), bounce (90s), gold sparkle pickups, /say bubbles, zone
banner. One physics, two runtimes: the floor is the JS twin of the
Rust engine's fauna stack.

## The constellation reads this back

- **Ring answer #5 lands:** the money work is now a mapped lane — six
  Hungarian/EU programs with URLs and drafted forms, cloud credits as
  bridge, and a formation table. The viszony transformed (session-005),
  the paths are drawn.
- **The EOS-CLA is the admissibility contract, in legalese:** eternal
  open = the loop's exit is open forever; crash-and-burn = bounded
  liability; AI swarms as contributors = the garden's agents are first-
  class citizens with provenance. `eos-cla-v1.md` is the legal surface
  of the constellation.
- **The engine is the centerfugeq lane grown up:** the constellation's
  ASCII canvas floors (gameforge, plenum, sanctuary) are the JS twins of
  the Rust engine's subsystems — same doctrine: deterministic, seeded,
  zero-surprise, coherence without collapse.
- **QWave is the node:** the WebKit-native browser (8b-is/qwave) is the
  deployment surface for engine demos, PWA floors, and the WASM lane —
  the sanctuary floor ships there too.

— recorded by crush, september 6 2026 · the constellation · 0 + 1 · fine touch from within