# Hub-and-Instance MMO Architecture — the Gemini planning session, synthesized

*An architecture-planning conversation (September 2026) recorded into the
8b-is research vault because it settles two open questions the engine's
roadmap had left open — the world structure (hubs vs instances) and the
server loop shape (Tokio event loop) — and because its honest parts agree
with what the engine already built, while its strongest disagreements
mark exactly where the engine must stay its own course.*

---

## the conversation's arc

The session ran from "UE + Rust + Go top-10 OSS libraries" through backend
sizing, a P2P/serverless detour, an all-Rust Bevy stack, a Tokio event-loop
skeleton, and landed on the participant's own game definition: **a mixture
of WoW, Diablo, Elder Scrolls, and platformers — an action-MMO-RPG where
the MMO part exists only in open-world cities, while levels and dungeons
are instanced (solo or party).** The closing directive: design the first
layer — input and content creation, from ideation to the mid-pipeline.

## the decisions worth keeping

### 1. the hub-and-instance world split

The participant's own sentence is the architecture: **cities are persistent
open-world social hubs; dungeons and levels are ephemeral instances.** The
session's mapping:

| Zone kind | Role | CCU | Tick rate | Lifecycle |
|---|---|---|---|---|
| **City hub** | social: trade, parties, quests, chat, cosmetics | 50–100 | 10–15 TPS | persistent process |
| **Dungeon instance** | action combat + platforming | 1–4 | 30–60 TPS | spun up on demand, destroyed when cleared or abandoned |

This sidesteps the seamless-10,000-player problem by construction, and it
matches the engine's floor design: the floors ARE instances, the sanctuary
IS a hub. The engine's design-v2 "world-as-DNS" (zone → Durable Object) is
this exact split with the serverless twist.

### 2. the server loop shape (Tokio event loop)

The session produced a concrete skeleton the engine's v1.x server core
should adopt in Rust form:

- **zero-lock main loop** — client reader tasks push into a central
  `mpsc::channel<ServerCommand>`; the tick loop owns the world state;
- **`tokio::select!`** — fixed-frequency tick (20–50 Hz) vs inbound
  commands, no thread blocking on state computation;
- **length-prefix framing** — 4-byte big-endian length header; the engine
  already has this exact discipline in `vaked-lsp/src/frame.rs` (the
  Content-Length door);
- **hub mode vs instance mode** — the same binary, two tick profiles: hub
  = broadcast routing + DB sync at 10–15 TPS; instance = deterministic
  state updates + collision at 30–60 TPS;
- **per-zone lifecycle** — empty zone spins down; party entering spins the
  instance up and hands back the address. The engine's answer: zones are
  actor subjects on the mesh; the GAIA seed makes zone state re-derivable,
  so spin-up is fold-from-seed, not cold load.

### 3. determinism and input sequencing

Fixed-timestep accumulator (64 Hz physics regardless of render FPS),
client inputs tagged with a monotonically increasing sequence number,
client prediction + server reconciliation with corrections on drift. The
engine's keeper already enforces the monotonic sequence — `t` on the wire
— and the roadmap's "deterministic lockstep where it pays" is exactly
this, now with the numbers attached.

### 4. the shared-crate superpower

All-Rust means one crate for `PlayerPosition`, `ItemData`, packet enums —
zero schema drift. The engine built this already: `crates/world-core`
(tern + GAIA + the fold) compiles to native AND wasm32, and the client
calls `gaia_wire_c`. The conversation independently arrived at the same
move the engine made first.

## where the engine disagrees (and must stay its own course)

| The session's advice | The engine's decision | Why |
|---|---|---|
| Bevy client, all-Rust | HTML + CSS + WASM client, Tauri shell for Steam | the floors are the live client; Bevy stays an integration seam, not the shipping frontend — pixels are a plug-in |
| Go for the network stack (earlier) | Rust world-core + the NATS mesh; Go only in the multiplexer lane | the mesh subjects ARE the zones; a second language re-introduces the schema drift the shared crate removed |
| PostgreSQL/SQLx + Redis for persistence | the ledger + `fold(seed, H) = M` + refusals durable | persistence is the committed log, not a state cache; Redis-style session state is the material fold, re-derivable |
| Agones/Kubernetes orchestration | serverless zones (Cloudflare Durable Objects in v2.x), NATS as the orchestration layer | the mesh already does spin-up/spin-down by subject; k8s is the heavier answer to the same question |
| P2P/serverless "zero infra" | the hybrid: developer-run lightweight zone nodes + DHT/master list later | the session itself concludes pure P2P fails at MMO scale (anti-cheat, asymmetric bandwidth, host migration) — the engine's protector node is the authority answer |

## the layer-1 design directive (the closing ask)

"Design the first layer — input and content creation, from idea generation
and ideation to the mid-pipeline." The engine's answer exists across four
repos and is now documented as
`8b-is-engine/docs/first-layer-content-creation.md`: the brief is the
input; GAIA turns it into a seed; the creative swarm fans it out; the
diffuser renders concept art; the vision lane QAs it; `gen.ts` turns the
admitted brief into a manifest; the scene builders turn the manifest into
Blender/Unity renders. Every stage is an **attested inscription** (the
keeper's discipline), and every label is a **named region, not a
mechanism** (the witness/fiber discipline) — the two new theories applied
to content creation itself.

## the open questions

1. **Hub tick profile**: what does 10–15 TPS mean for the mesh — batched
   deltas per 100 ms window, or event-driven chat-only flow?
2. **Instance spin-up from seed**: how fast can fold-from-seed spin an
   instance up vs loading a checkpoint — and when does a checkpoint win?
3. **Input sequencing vs the keeper's tick**: the session's `u64` sequence
   and the wire's `t` — one field or two (network sequence vs world tick)?
4. **The mid-pipeline boundary**: where exactly does "content creation"
   end and "simulation" begin — at the manifest, at the first admitted
   delta, or at the first render that passes vision QA?

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*
