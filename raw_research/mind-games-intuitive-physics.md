# Mind Games — Game Engines as an Architecture for Intuitive Physics

*Ullman, Spelke, Battaglia & Tenenbaum (MIT/Harvard/DeepMind, 2017).
Recorded because it is the theoretical backbone of the engine's physics:
the "mental physics engine" hypothesis is, point for point, what
centerfugeq + the trick library already do — approximate, fast, plausible
dynamics over veridical simulation.*

---

## the thesis

Human intuitive physics is a **mental physics engine**: not a molecular
simulation, not a neural net over pixels, but a game-engine-style
simulation that parcels the world into **objects** with **properties** and
**events**, then evolves them forward with **approximations and hacks**
that look right rather than being right.

> "the models don't have to be accurate in any sense that physicists would
> recognize; they just have to produce results that look reasonable... fast
> – faster than real time... on low power circuitry — a brain, or a smart
> phone."

This is the engine's doctrine, verbatim: **coherence without collapse.**
Rapier3D + SDF raymarching, over-relaxed sphere tracing (ω = 1.2),
quarter-res + temporal reprojection — all hacks that produce *plausible*
dynamics in real time, not exact ones.

## the concepts, mapped to the 8b-is engine

| Physics-engine concept | The 8b-is engine |
|---|---|
| **objects + events** (bounded chunks in space; delimiting points in time) | the entity + the EventBus; every actor is an object, every collision an event |
| **static vs dynamic** (background vs simulated) | zones (Durable Objects, the ground) vs entities (actors) |
| **sleeping vs awake** (skip bodies at rest; wake on collision) | the 0-alloc tick loop — don't simulate what isn't moving; the fauna wakes on the hum |
| **body vs shape** (cheap physics proxy vs rendered mesh) | the SDF *body* vs the rendered *shape* — "one physics, two runtimes"; the floor is the JS twin of the same body |
| **collision detection as a separate module** (bounding box, not exact shape) | the AABB pre-pass before sphere tracing |
| **constraints** (hinge/rod/axle; glue bodies without force sim) | the warp tensors, geodesic vector gravity, the terraced geometric joints |
| **hard / soft / stuff** (rigid, soft, fluid — escalating cost) | the fauna 5-layer: rigid bestiary → soft → the field (fluid) |
| **the hacks** (qualitative switches, no scientific basis) | the trick library — branchless abs, gray deltas, tables over branches |

The paper's central contrast — photons/molecules (too slow) vs
pixel-vectors (no objects) vs the physics engine (object-factorized
middle) — is exactly our position: **centerfugeq's quantPhysics is the
middle way.** The Ising/kuramoto/halo lanes factor the world into
coherent objects (wells, oscillators, halos) and evolve them with seeded,
replayable hacks, never a molecular sim, never a latent-vector guess.

## the four implications for the engine

1. **Objects are the unit, not pixels.** The world-model's needs/goals
   scheduler (the Dwarf-Fortress clock) runs on *objects with properties*,
   not on a rendering.
2. **Sleep/wake is a physics rule, not an optimization.** The proto's
   `ACTOR_CRASHED`/`ACTOR_RESPAWNED` and the sleeping/waking fauna are the
   same computation: skip the still, wake the struck.
3. **Body ≠ shape is our "one physics, two runtimes."** The SDF body is
   the truth; the rendered shape (wgpu / Blender / Unity / UE) is the
   display. Four engines, one body.
4. **The hacks are the point.** "Take the trick, not the engine" — the
   demoscene lane and the trick library are not aesthetic; they are the
   physics engine's honest working set, the same hacks the paper argues
   the human mind runs.

---

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*