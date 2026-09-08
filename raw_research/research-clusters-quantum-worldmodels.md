# Research clusters — quantum geometry & learned world models

*Two deep-research clusters from the parallel search program, recorded for
the engine's theory. clusterF: quantum-state geometry and its (lack of) a
bridge to game worlds. clusterB: learned world models, state vs. rendered
content. The negative finding in F is the most valuable result: it keeps
the synthesis honest.*

---

## cluster F — quantum geometry (53-row matrix, cited in the source session)

**Rigorously established:**

- **State-space geometry** — pure states as a Kähler/projective Hilbert
  manifold with Schrödinger flow as Hamiltonian dynamics; mixed states as a
  convex body; arbitrary compact convex state spaces in generalized
  probabilistic theories (GPTs).
- **Admissible transformations** — positive/CP normalization-preserving
  maps as the theory-defining choice; higher-order transformations via
  quantum combs; no fixed transition order via the causaloid.
- **Measurement as intervention** — instruments and interventionist quantum
  causal models: the closest rigorous analogue of "observation as selection
  among admissible trajectories."
- **Information metric** — classical uniqueness (Čencov/Campbell) vs. a
  quantum family of monotone metrics; monotonicity means the metric is
  defined by how admissible transitions act on it.
- **Compositionality** — dagger-compact process theories; the CQM ↔
  convex-operational bridge.
- **Strongest real bridge to transition systems** — Markov categories and
  string-diagrammatic Bayesian inversion put classical stochastic
  state/transition systems in the same categorical language as quantum
  processes; the information geometry of Markov kernels gives a geometry of
  the transition structure itself.

**The explicit negative finding:**

> No established literature directly unifies quantum-state geometry with
> persistent virtual worlds or learned game engines. The defensible
> connection passes through generalized operational theories, compositional
> process formalisms, Markov categories, and classical information geometry.
> The proposed synthesis is a **new transfer of formal structure**, not a
> report of an existing interdisciplinary field.

**The bridge chain that IS defensible:**

```
quantum state geometry
  ↔ process theories (dagger-compact)
  ↔ Markov categories
  ↔ classical transition systems
  ↔ world models and simulated worlds
```

**Terminological trap flagged:** "game semantics" (Clairambault et al.) is
about logical interaction protocols, not video games — must not be cited as
a quantum↔video-game link.

## cluster B — learned world models (31 verified sources)

**The core distinction:**

- **Latent-state predictive world models** commit to a state $s_t$, a
  learned transition $p(s_{t+1} \mid s_t, a_t)$, and a consumer (a planner
  or an imagination-trained actor-critic): World Models, PlaNet, Dreamer
  v1–v3/Nature (Nature 640:647–653), MuZero, IRIS, DIAMOND, Dreamer 4,
  Playable Environments (arXiv:2203.01914), Navigation World Models
  (arXiv:2412.03572), UniSim. The state space is the space of possible
  states; the transition model is the admissible-transition relation.
- **Action-conditioned rendering, no stated state** — autoregressive frame
  predictors: GameNGen (Stable Diffusion compression latent, not a state
  latent), Genie (the hinge case; PMLR v235, ICML 2024 Best Paper),
  Genie 2/3, Oasis, GameGen-X, Hunyuan-GameCraft, The Matrix, GameFactory,
  GameGAN. A Jan-2026 taxonomy names the gap: "stateless" video
  architectures vs. state-centric world-model theory.

**Two findings that matter for the engine:**

1. **Persistence is always engineered, never free.** The persistence
   papers converge on storing state (pose, timestamp, geometry) alongside
   pixels — WorldMem's memory units, Genie 3's ~1 min visual memory, Oasis's
   "limited memory over long horizons." This is the engine's thesis,
   empirically confirmed: a *ledger* must exist; it never emerges from
   rendering.
2. **The empirical ceiling** — video diffusion models fail out-of-distribution
   with nearest-example imitation (unfixed by scaling), and physical
   understanding is "unrelated to visual realism" — against a theoretical
   result that any agent generalizing to multi-step goal-directed tasks
   must contain a predictive model.

**Flagged not peer-reviewed:** Genie 2/3, Project Genie, Oasis, Cosmos,
Dreamer 4, Hunyuan-GameCraft-2 (technical report), 2025–26 preprints.

## what the engine takes

1. The theory's claim is a **transfer, not a discovery**: persistent worlds
   as compositional state-transition systems with admissibility and
   intervention — quantum theory is one developed *example*, not the
   explanation. Haplopraxis, Spherepop, RSVP sit on the classical/
   generalized-process side.
2. **"State or rendering?" is the load-bearing distinction** — exactly the
   engine's inscription (ledger state) vs. render (on-demand frames). The
   learned models that keep state (Dreamer, DIAMOND) are the wiring-ins;
   the renderers (GameNGen, Genie, Oasis) are prototyping references.
3. **Persistence is engineered** — the ledger/JetStream/bitemporal store is
   not a feature; it is the whole point, and no generative system provides
   it for free.

---

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*