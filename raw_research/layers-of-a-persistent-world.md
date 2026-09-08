# Layers of a Persistent World — rendering, operative state, provenance, committed history

*Flyxion, September 2026. Recorded because it is the engine's
architecture, formalized: the four-layer separation that makes a world
*persistent* rather than merely controllable. Every prior doc (theory,
actor-mesh, world-models) converges here.*

> **The central principle:** history is authoritative at commitment
> boundaries; state is authoritative between them.

---

## the layers question

The word "state" is used for four different things. Separating them is the
whole architecture:

| Layer | What it is | Authority | Typical failure |
|---|---|---|---|
| **rendering** | observer-relative appearance | none beyond presentation | visual continuity mistaken for world continuity |
| **operative state M** | fields, objects, variables the dynamics need now | provisional | snapshot treated as complete identity |
| **provenance state Q** | ownership, permissions, attributions, scars | certified historical projection | context recomputed informally or lost |
| **committed history H** | typed event DAG (append-only) | **identity + admissibility** | past silently patched after divergence |

> rendered appearance ≠ operative state ≠ provenance state ≠ committed
> history. Not four worlds — four roles in one architecture.

## one history, several folds

Current state is a *certified cache* over the history — history is
authoritative without replaying the whole past per frame:

$$M_t = \text{fold}(\text{commit}_{phys}, M_0, H_t)$$
$$Q_t = \text{fold}(\text{commit}_{prov}, Q_0, H_t)$$

Other folds (accounting, narrative, measurement, observer indexes) are
free. The world is not a snapshot paired with a log; it is the log plus a
family of certified folds and checkpoints.

## observation ≠ attestation

- **looking**: $R(M_t, Q_t, \omega) \to x$ — disposable, creates no history.
- **attesting**: $(x, \text{witness}, \text{rule}) \to E_{t+1} \to$ narrower
  admissible set.

A screenshot must not alter a world; a signed measurement used to
authorize a repair can. The decisive property is not perceptual
occurrence but *constraining work*.

## admission, refusal, repair

A history of only successes is incomplete. Refusals disclose boundaries.
The event vocabulary must include `proposed, admitted, refused, repaired,
replay-discrepant`:

$$c \to \text{gate}(c \mid M_t, Q_t, H_t) \to \{\text{admit}, \text{refuse}, \text{repair}\}$$

The physical fold ignores a refusal (no admitted change); the provenance
fold records it (an intrusion can alter suspicion/audit/future
admissibility). **Never repair the past in place** — append.

## checkpoints & replay divergence

Checkpoints are accelerators, not rival authorities:
$C_k = (\text{frontier}, M_k, Q_k, \text{versions}, \text{seeds}, \text{hash})$.
When bitwise replay fails (solver drift, hardware, corruption): **append a
replay-discrepancy event** with expected/obtained hashes + disposition.
The system may improve; it may not present the improvement as if it had
always been the original. Epistemic immutability ≠ operational rigidity.

## distributed worlds = causal DAG history

No single total order everywhere. Commits name their causal frontier;
independent events commute, conflicting ones cannot:

$$e_i \perp e_j \implies \text{fold}(e_i;e_j) = \text{fold}(e_j;e_i)$$

Chandy–Lamport marks the epistemic ceiling: a globally consistent snapshot
may match no instantaneous state. Competing actions must be ordered,
refused, branched, or repaired — never declared independent for
convenience.

## what is new (the honest claim)

No located literature unifies persistent-world engineering, learned world
models, provenance-sensitive rendering, refusal-aware history, and
operational geometry. The contribution is a **transfer of shared formal
vocabulary**, not "games are quantum." The hierarchy of claims:
**renderability < controllability < recurrence < provenance <
persistence** — persistence means identity survives change because
commitments *and refusals* remain addressable.

## the design rules (engine-ready)

1. **Rendering is pure** — a render reads certified folds, writes nothing.
2. **Commit attestations, not perceptions.**
3. **Typed events** — proposals/admissions/refusals/repairs/attestations/
   checkpoints/discrepancies are distinct kinds.
4. **Derive current authority** — M and Q are folds over H, checkpointed.
5. **Refusal is durable** — a failed proposal may leave physics unchanged
   yet still alter the audit/provenance fold.
6. **Never patch the past** — corrections are appended with their relation
   to the failed event.
7. **Record causal parents** — independent events commute; dependent ones
   cannot.
8. **Separate recurrence levels** — bitwise ≠ numerical ≠ semantic ≠
   provenance equivalence.

## addendum — the observer's architecture + the wall's two memories

The full paper adds a section the first recording compressed: the layering
applies on **both sides of R(M_t, Q_t, ω_t)**.

- **The observer needs a history too.** de Gyurky & Tarbell's *The
  Autonomous System* (2014) maps Kant/Hegel/Schopenhauer to a subsystem
  constellation. **Presentation** = appearance (the world as rendered to a
  subject); the **noumenon** machinery = the agent's model of M_t — two
  layers, kept apart by the Kantian inheritance. The **Intellect** is the
  librarian: **abstract knowledge** = a declared record (secondhand),
  **experiential** = a witnessed record, **practical** = declared
  constrained by witnessed (attestation — constraint-without-erasure, in
  the agent). Its defect: the databases are updated *in place* — a fold
  without a log. Schopenhauer's epigraph: a system of thoughts must have an
  architectural structure — three layers on the observer's side too.
- **The wall's two memories.** **Material memory** (what the field carries:
  cracks, deformation — M_t, Markov) vs **historical memory** (who built
  it, what happened, whether a repair is original, ownership — H_t read
  through Q_t). Rendering consults both: an observer encounters a
  historically *situated* object. Two separate folds, one history — a
  single event is admitted or refused once, each fold consumes the outcome.
- **Persistence is engineered.** Renderability < controllability <
  recurrence < provenance < persistence. Frame-predictors have #1;
  control-models have #1–2; a checkpointed deterministic engine has #3;
  **nothing surveyed has #4–5** — and #5 (persistence) is what "persistent"
  should mean.

The paper's open questions §16 — event-vocabulary minimality, commute
certification, graded replay equivalence, learned-models-without-ledgers,
refusal-vs-permission poisoning, viability over (M_t, Q_t), the
snapshot-collapse information metric — are the engine's next research
targets.

---

---

## what this means for the engine

| Flyxion layer | the 8b-is engine |
|---|---|
| **rendering** | the floors + wgpu/Blender/Unity/UE surfaces — renders of the seed, disposable |
| **operative state M** | the world-model's live fields (the NPC needs, the fauna, the zone tick) |
| **provenance state Q** | the sovereign pass, the reputation graph (bhava/Fable), permissions, the scars |
| **committed history H** | the JetStream/bitemporal ledger — the actor-mesh's `ledger.<stream>` subjects, the DAG |
| $M = \text{fold}(H)$ | the deterministic replay: the seed + the ledger → the same world (Recurrence) |
| **refusal durable** | the sovereign gate's *denials* are events, appended, never erased |
| **replay discrepancy** | our "replayable ⇒ admissible": a failed replay is appended as a discrepancy, not patched |
| **causal DAG** | the NATS mesh — each commit names its frontier; zones fold independently where events commute |

The report closes a loop this session opened: the research clusters
(quantum geometry + world models) found the *rigor*; the actor-mesh
design sketched the *shape*; Flyxion's four layers are the *law*. The
engine was already pointing there — now it has the formal statement:
**a world persists not because it renders the same scene again, but
because it can state what was committed, what was refused, and why the
present is entitled to count as a continuation of its past.**

---

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*