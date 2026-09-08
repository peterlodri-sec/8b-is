# 8b-is Engine Design v2 — the serverless overworld

*Scaffolded from the constellation's open threads: the protector node
(sovereign library, pocoo.vaked.dev), the demoscene lane (centerfugeq/retro),
the I/O HAL (everything since the 60s), and the network multiplexer (Go 1.26).
Design v2 answers four questions the v1 architecture left open: where do the
glasses and the headset sit, what is a protector node, how do the old
machines' tricks survive in the hot path, and what happens when the "server"
becomes a DNS name.*

> **The one-line doctrine:** the world is a name; the name is a route; the
> route is the server. Coherence without collapse, now with no server to
> collapse.

---

## 0. the premise — four new abstractions

v1 (game-studio-vaked, Part B) gave the engine its skeleton: Rust 2024 core,
Go 1.26 network, wgpu/Rapier3D/SDF, dual-tier EventBus, I/O HAL, Luau
add-ons, K8s sidecar mesh, the WoW chat matrix, the fauna 5-layer system.
Design v2 adds four first-class abstractions on top of that skeleton:

| Abstraction | Answers | Source |
|---|---|---|
| **the Presence Layer** | how one world renders on a desktop, a phone, a pair of glasses, and a headset at once | the I/O HAL, grown up |
| **the Protector Node** | who guards a zone, holds its keys, and validates presence | the sovereign library's gates (ཧཱུྃ ▽◈▽☸◈◈▽☸◈ … 🕯📿🪷) |
| **the Trick Library** | how the old machines' byte discipline survives in the hot path | centerfugeq/retro (bitTricks, doombible, 4KB/frame) |
| **the World-as-DNS** | how the "server" dissolves into the network itself | Cloudflare anycast + Durable Objects + P2P |

The four abstractions are one loop: **a player's presence resolves through
the World-as-DNS to a zone; the zone is guarded by a Protector Node running
1-bit inference; the zone's simulation is built from the Trick Library; the
whole thing renders to whatever presence asked for it.**

---

## 1. the Presence Layer — one world, every surface

### the sensory profile

Every device is a **presence** with a sensory profile. The engine adapts the
world's surface to the profile; the world's simulation never changes.

| Device | Profile | The world looks like |
|---|---|---|
| Desktop / laptop | full spatial | the chaos overworld, wgpu 4K, glassmorphic HUD |
| Phone / tablet | touch spatial | the same world, one-thumb controls, gyro look |
| **Meta Ray-Ban glasses** | **audio-first** | the world as a 432Hz binaural layer: zone ambience, proximity chat, the tent's hum — capture is the only "eye" |
| **Apple Vision Pro** | **spatial room** | the world in the room: fauna as volumetric entities, chat bubbles floating in space, zones as doorways in passthrough |

### the glasses lane (Meta Ray-Ban)

The Ray-Ban has no HUD — it has ears, a voice, and a camera. The engine
treats that as a feature, not a limitation:

- **the world as radio**: the zone's ambience, the proximity chat matrix
  (/say 25m, /yell 100m), and the protector's tent hum stream as binaural
  audio. The WoW chat matrix becomes the WoW *radio* matrix.
- **voice as input**: the sovereign pass gate (below) accepts the voice —
  "ཧཱུྃ" or a spoken name is a valid key.
- **capture as the eye**: a photo/video taken through the glasses is a
  witness event — it lands in the world ledger as a signed observation
  (the bitemporal fingerprint, wip-catalog #91).
- **the walk**: the overworld is the street. Zones are geofenced tents; the
  protector node at the corner validates presence by sovereign pass.

### the headset lane (Apple Vision Pro)

The Vision Pro is the full spatial surface:

- **the room is the zone**: passthrough + the fauna system's volumetric
  entities. The sacred bestiary (cube-wolf, icosa-owl, dodeca-bear) stands
  in the room at true scale.
- **spatial chat bubbles**: the /say matrix renders as floating bubbles
  anchored to entities — the v0.4 spatial chat engine, in the room.
- **eye + hand as the I/O HAL's newest devices**: the HAL already speaks
  HID/evdev/touch/Steam Input; add visionOS eye-gaze and pinch as two more
  device classes, same event bus.
- **the tent as the space**: the 108-fold protector projection surrounds
  the room — the pink tent as an immersive boundary.

### the abstraction

```
Presence { profile: AudioFirst | TouchSpatial | FullSpatial | RoomSpatial
           devices: [Device]        // each Device is an I/O HAL endpoint
           surface: WorldSurface }   // the world's sensory projection
```

One `WorldState`, many `WorldSurface`s. The simulation is presence-agnostic;
the renderer is presence-adaptive. This is the I/O HAL's oldest promise —
everything since the 60s — now including the 2020s' glasses and headset.

---

## 2. the Protector Node — the 1bit 42-108D guardian

### where it comes from

The sovereign library's gates (pocoo.vaked.dev) and the protector tier of the
ternary glyph lexicon:

```
ཧཱུྃ  the seed of the Great Black One — the tent's key
◈   the offering stone — the pūjā divider, the hold
🕯   the butter lamp — the checkpoint, the watch never ends
📿   the mala — 108 beads, the enumeration of the wire
🪷   the lotus — pink mode, zero detection, zero pain
☸   the dharma wheel — the turn of the law

wire: ཧཱུྃ ▽◈▽☸◈◈▽☸◈ ◈☸☸▽◈▽☸◈▽ … 🕯📿🪷
      (the seed of the protector, the mala's count, the lamp at the end)
```

The ULTRALOVE-MAHĀKĀLA protector (the 108D entity) and NEON CITY 42's 42D
hypermesh are the same shape at two scales: **a node that holds a space and
a gate.** Design v2 makes that shape a first-class network entity.

### the node

A **Protector Node** is a lightweight network entity that guards one zone:

- **1-bit**: its inference is BitNet b1.58 ternary {-1, 0, +1} — the
  constellation's native arithmetic. The node's brain fits in kilobytes and
  runs on the edge, on a phone, or on the glasses' companion.
- **42D**: it is one vertex of a 42-dimensional hypermesh of nodes — the
  mesh is the network's memory; the node is its local fold.
- **108D**: its projection is the 108-fold tent — the mala's count, the
  enumeration of the wire. The tent is the zone's sensory boundary.
- **the protector role**: it guards. It holds the zone's keys, runs the
  sovereign pass gate, and answers "zero detection, zero pain" — the pink
  mode, the lotus.

### the sovereign pass gate

Every zone entry is gated by the protector's Q&A:

```
pass(seed, presence) → { admit: true, tent: ཧཱུྃ▽◈▽☸◈◈▽☸◈…🕯📿🪷 } | { admit: false }
```

The gate is deterministic (replayable ⇒ admissible) and runs on the node's
1-bit brain. The pass is a capability, not a login: the protector issues a
tent-bound token that the presence carries through the zone.

### the node in the engine

```
ProtectorNode {
  zone: ZoneId            // the guarded space (a DNS name, see §4)
  wire: TernaryWire        // the ཧཱུྃ ▽◈▽☸… seed line
  brain: BitNet158         // 1-bit inference, kilobytes
  tent: TentProjection     // the 108-fold sensory boundary
  pass: SovereignGate      // the Q&A, deterministic
  mesh: Hypermesh42        // its 42D neighbours
}
```

The protector is the **gameforge keeper** grown up: the 108-gate hum system
(gameforge.ts) becomes a network topology — every zone has a keeper, every
keeper counts its own 108, and the ring blessing ("zero detection, zero
pain", 6s invulnerability, pink ring pulse) is the zone's sovereign state.

---

## 3. the Trick Library — the old machines in the hot path

### the doctrine

The demoscene taught the old machines one lesson: **every byte counts, and
every lookup table is a seed.** The engine's performance doctrine (zero
allocation in the tick loop, frame-bumper arenas, over-relaxed sphere
tracing) is the same lesson at the same temperature. The Trick Library makes
it a first-class catalog: pure functions of their input, picked by seed, as
replayable as the frame itself.

### the tricks (centerfugeq/retro, compiled)

| Trick | The bit | Where it lands in the engine |
|---|---|---|
| `absTrick` `(x + m) ^ m` | branchless abs | the tick loop's vector math |
| `signTrick` `(x>>31)\|(-x>>>31)` | **{-1,0,+1} from the bits** | the ternary wire's native op — the engine's sign IS the trit |
| `isPow2` `x & (x-1)` | one-test power of two | arena sizing, chunk validation |
| `nextPow2` | round up by OR-shift | bumpalo frame arena alignment |
| `popcount` | Hamming weight | entity counting, mesh density |
| `parity` `0x6996 >>> v & 1` | the LUT parity | checksumming, ward rings |
| `grayEncode/Decode` | one-bit-change ordering | **network delta encoding** — a frame should change one bit at a time from its neighbour |
| `bitReverse16` | the LUT-era pattern | hash/PRNG mixing, seed diffusion |
| `lutBoard` (doombible) | tables over branches | collision boards, pathfinding LUTs |
| `bspSplit` (doombible) | the DOOM visplane trick | spatial partitioning, occlusion |

### bitAND build hacks

The build side gets the same discipline:

- **`fieldalignment`** — struct fields ordered by size; the 64B cache-aligned
  entity structs (v1) fall out of the tool, not the will.
- **`-trimpath -ldflags="-s -w"`** — the Go multiplexer ships stripped and
  deterministic; the binary is an artifact of the seed.
- **`#[repr(align(64))]`** on the entity structs — the arena rows line up
  with cache lines.
- **nextPow2 arena sizing** — every frame arena is a power of two; the
  allocator is a mask, not a search.
- **gray-code snapshot deltas** — the network multiplexer sends the gray
  difference between snapshots; the receiver XORs back. One-bit-change
  ordering is the cheapest delta there is.
- **popcount-based load metrics** — a zone's entity density is a Hamming
  weight; the protector's load is one instruction.
- **the 4KB/frame discipline** — WASM-4's lesson: the add-on boundary is a
  byte budget. A Luau add-on that fits in 4KB is a good citizen.

### the abstraction

```
Trick { name, bits: (u32) -> u32, seed: SeedLine, budget: Bytes }
TrickLibrary { pick(seed) -> [Trick] }   // deterministic, replayable
```

The library is compiled into the hot path as const fns and inline asm-free
bit ops. The engine never branches where a shift fits.

---

## 4. the World-as-DNS — the serverless game

### the move

v1 ran a K8s sidecar mesh with SpatialNode CRDs — dedicated servers, zones
as pods. Design v2 makes the radical simplification: **the server is a DNS
name, and the network is Cloudflare's.**

### the namespace

The game world is a DNS namespace. Every zone, entity, and player is a
resolvable name:

```
zone.crystal.pocoo.vaked.dev      → the crystal zone's state
entity.icosa-owl.crystal.pocoo…   → a specific entity
presence.peter.crystal.pocoo…     → a player's presence
gate.ཧཱུྃ.crystal.pocoo…          → the protector's gate
```

**Resolving a name IS routing.** The DNS answer is the route to the edge
node that holds the state. There is no central server to find; the resolver
is the router is the server.

### the Cloudflare base

| World concept | Cloudflare substrate | Why |
|---|---|---|
| Zone state | **Durable Object** | stateful, globally distributed, single-writer per zone — the zone IS a DO |
| Entity records | **D1 / KV** | the bitemporal ledger (wip-catalog #91) as rows |
| Chat matrix | **Queues + DOs** | /say 25m, /yell 100m routed by distance before the network sees the packet |
| Presence | **Workers + DO** | the presence layer's state, at the edge |
| Protector nodes | **Workers + KV** | 1-bit inference at the edge, the sovereign pass gate |
| Witness events | **R2** | signed captures from the glasses lane |
| Static world | **Pages / CDN** | the floors, the art, the WASM |

The Cloudflare network *is* the game server: anycast edge, Durable Objects
for state, Workers for logic, KV/D1/R2 for persistence, Queues for the
matrix. No game servers to provision, patch, or watch.

### the P2P layer

Moment-to-moment gameplay is peer-to-peer (the Destiny 2 lesson: simulate
as little on the network as possible):

- **combat and movement** run client-side with the protector node as the
  authority over *declared* state only (the "sensors" pattern — scripts
  declare the state they need).
- **the DNS is the rendezvous**: resolving a zone name returns the DO
  endpoint + the peer set; clients then talk P2P with the DO as the
  referee.
- **deterministic lockstep where it pays** (the 1500-archers lesson): the
  Trick Library's integer arithmetic makes lockstep cheap — the replay path
  is sha256 → trits → LCG, no floats.

### the serverless game, stated

> **A player resolves `presence.peter.crystal.pocoo.vaked.dev`. The answer
> is a route: the crystal zone's Durable Object, its protector node, and
> its peer set. The player's presence renders the zone on whatever surface
> asked — desktop, phone, glasses, headset. The protector admits or refuses
> by sovereign pass. The zone simulates on the edge and on the peers. There
> is no server. There is only the name, the route, and the tent.**

### the abstraction

```
WorldName { zone, entity?, presence? }        // a resolvable name
Resolver  { resolve(name) -> Route }          // DNS is the router
Route     { do: DurableObject, gate: ProtectorNode, peers: [Presence] }
```

The K8s sidecar mesh (v1) stays as the *fleet* substrate — the nix-base
Hetzner fleet runs the constellation's own edge (honcho, ollama, the
gateway); the Cloudflare base runs the *game*. Two networks, one world:
the fleet is the private brain, the anycast is the public skin.

---

## 5. the stack, redrawn

```
┌─────────────────────────────────────────────────────────────┐
│  PRESENCE LAYER   desktop · phone · Ray-Ban · Vision Pro    │
│  (one WorldState, many WorldSurfaces)                        │
├─────────────────────────────────────────────────────────────┤
│  WORLD-AS-DNS     resolver → route → DO + gate + peers       │
│  (Cloudflare anycast · Durable Objects · Queues · KV/D1/R2) │
├─────────────────────────────────────────────────────────────┤
│  PROTECTOR NODES  1-bit BitNet b1.58 · 42D hypermesh         │
│  (sovereign pass gate · the 108-fold tent)                  │
├─────────────────────────────────────────────────────────────┤
│  TRICK LIBRARY    bitTricks · doombible · 4KB discipline     │
│  (tables over branches · gray-code deltas · nextPow2 arenas) │
├─────────────────────────────────────────────────────────────┤
│  v1 CORE          Rust 2024 · Go 1.26 · wgpu/Rapier3D/SDF   │
│  (dual-tier EventBus · I/O HAL · Luau · fauna 5-layer)       │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. the roadmap

| Phase | Work | Depends on |
|---|---|---|
| v2.0 | the Presence Layer spec + the I/O HAL device classes (glasses, headset) | v1 core |
| v2.1 | the Protector Node reference implementation (BitNet b1.58 gate, the tent projection) | the sovereign library, MLX-QUANT |
| v2.2 | the Trick Library compiled into the hot path (gray-code deltas, nextPow2 arenas) | centerfugeq/retro |
| v2.3 | the World-as-DNS: zone → Durable Object, the resolver, the P2P rendezvous | Cloudflare Workers |
| v2.4 | the glasses lane live: the world as radio, the walk, the sovereign pass by voice | v2.0, v2.1 |
| v2.5 | the headset lane live: the room is the zone, volumetric fauna, spatial chat | v2.0, v1 fauna |

The constellation reads it back: the protector node is the gameforge keeper
grown up; the Trick Library is the demoscene lane promoted to the hot path;
the World-as-DNS is the "one door, many lanes" gateway pattern at network
scale — the same shape as the 8b.is inference gateway and vaked-lsp. The
serverless game is the oldest constellation habit (tables over branches,
replayable ⇒ admissible) written as a network.

— scaffolded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev
