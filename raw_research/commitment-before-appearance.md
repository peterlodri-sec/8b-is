# Commitment Before Appearance — Event Histories, Material State, and the Two Folds of a Layered World

*Flyxion, independent researcher, September 2026. Recorded into the 8b-is
research vault because it is the engine's architecture, formalized: one
append-only log, two folds — a physical fold for the operative world and a
semantic fold for provenance and admissibility — with attestation as the
only bridge from a disposable look to a durable constraint. The keeper,
GAIA, and the replay verification already implement every equation in this
paper; the paper supplies the jurisdiction language the code was missing.*

---

## the unresolved question beneath layering

Order and Obfuscation taught that abstraction relocates difficulty rather
than annihilating it. Layering appearance, state, and history tempts a
simple stack — $H_{\le t} \to M_t \to x_t$ — which is ambiguous and worse,
suggests history is merely a deeper state continuously consulted by the
layers above, making an append-only log the hidden implementation of every
frame and **turning every act of viewing into a possible historical
mutation**. The correction is to distinguish **authority from access**: a
legal archive is authoritative for title without being reread whenever a
door opens; a source repository is authoritative for provenance without
being replayed whenever a binary draws a pixel. The layering question is
not solved by choosing state or history as fundamental — it is solved by
assigning each a different **jurisdiction**.

## three objects and three kinds of authority

Let $H_t = (e_1, \dots, e_t)$ be the committed event history, $M_t$ the
cached material/operational state, $x_{t,\omega}$ an appearance under
transient viewing conditions $\omega$. History answers how the world
acquired its commitments and which distinctions remain recoverable;
material state answers what operational configuration is presently
available; appearance answers what a particular rendering exposes under
particular conditions. Authority is task-relative: $H_t$ for identity and
provenance, $M_t$ for operational rendering, $x_{t,\omega}$ only for the
delivered appearance.

This prevents two symmetric errors: **snapshot reductionism** ($M_t$ as a
sufficient replacement for its path) and **log absolutism** ($H_t$ as the
structure every present operation must recompute from). The first destroys
historical distinctions; the second confuses normative authority with an
inefficient access pattern.

> **Definition 1 (Historical authority).** A history $H_t$ is authoritative
> for a property $P$ when disputes about $P$ are settled by the committed
> events and their ordering, not by any lossy state derived from them.
>
> **Definition 2 (Operational authority).** A material state $M_t$ is
> authoritative for an operation $Q$ when the system may execute $Q$ against
> $M_t$ without replaying $H_t$, provided $M_t$ is certified as a valid fold
> of the relevant committed history.

A cache is not epistemically inferior because it is derived; its authority
is narrower — it governs rendering and interaction while remaining
revisable in light of the log.

## the event log is not a visual layer

"Below" is misleading; the relation is not spatial containment. The log and
the state need not share a schema or a file tree — the relation is an update
rule. With $U_M : M \times E \to M$:

$$M_t = \text{Fold}_M(H_t; M_0) = U_M(\cdots U_M(U_M(M_0, e_1), e_2) \cdots, e_t)$$

The formula specifies **legitimacy, not an access pattern**. Checkpoints,
snapshots, indexes, and incremental views are admissible because they
preserve the fold relation (distributed snapshots, database recovery — the
classical separations). Rendering then has the narrower form
$x_{t,\omega} = \text{Render}(M_t, \omega_t)$ — **not**
$\text{Render}(M_t, H_{\le t}, \omega_t)$ — which would grant the renderer
unnecessary archival jurisdiction and hide an unbounded computation inside
disposable surface work. If provenance must be displayed, its certificate
is part of the cached state supplied to the renderer; the renderer still
never interprets raw history.

## one log, two folds

The material state is not the only derived object. The same events support
a **semantic fold** $U_S : S \times E \to S$ preserving event identity,
provenance, refusal, dependency, custody, and constraints on later
admissibility: $S_t = \text{Fold}_S(H_t; S_0)$. The architecture is not one
long pipeline from history to picture but **two distinct reductions of the
same source**:

$$H_t \to M_t, \qquad H_t \to S_t, \qquad (M_t, \omega_t) \to x_{t,\omega}$$

The physical fold answers "what configuration have these commitments
produced?" The semantic fold answers "what do these commitments establish,
preserve, forbid, or leave unresolved?" The folds may coincide for simple
events, but nothing requires isomorphism: **a refusal may leave the visible
material state unchanged while altering the semantic record of
admissibility**; two histories may yield indistinguishable renders while
preserving different custody chains; several appearances may render from one
material state without generating any new commitment.

> **Principle 1 (Dual-fold authority).** Operational behavior is mediated by
> a validated material fold $M_t$; identity, provenance, and admissibility
> are adjudicated by a semantic fold $S_t$ or, when necessary, by the
> underlying history. Neither fold may silently substitute for the other.

This supplies a precise meaning for cache validity: a checkpoint $C_t$ at
event position $k \le t$ legitimizes $M_t = \text{Fold}_M((e_{k+1}, \dots,
e_t); C_t)$ exactly when $C_t$ is certified to equal $\text{Fold}_M(H_k;
M_0)$. State can be fast without becoming historically ungrounded.

## looking is not an event

In graphics, observation means sampling or rendering; in epistemic and
legal settings, it may mean registering evidence that changes what later
claims remain defensible. These are not the same operation. Changing
$\omega_t$ — rotating a camera, filtering a signal, running a diagnostic —
is transient; unless committed, it does not extend $H_t$. If every look
appended an event, historical growth would depend on observer count,
refresh rate, debugging activity, and UI design; two otherwise identical
worlds would acquire different identities merely because one was watched
more often.

The necessary boundary is **attestation**: an observation $o$ plus an
attestation $a$ (agent, method, scope, asserted evidential consequence)
becomes a candidate event $e_{t+1} = \text{Attest}(o, a)$ only when accepted
under the world's commit rule; once committed it may narrow the admissible
continuation set $A_{t+1} = \{c \in A_t : c \text{ compatible with } e_{t+1}\}$.
The observation matters historically because it has been made **answerable**,
not because photons reached an eye or values reached a screen.

> **Principle 2 (Attestation boundary).** Rendering, sampling, and
> inspection are disposable computations. An observation becomes a
> historical event only when it is attested and accepted as a constraint on
> subsequent admissibility.

Attestation is not infallibility: a committed report may later be
challenged or superseded; its historical identity remains the identity of a
particular claim made under particular conditions. Later evidence changes
the admissible interpretation without rewriting that it was made — exactly
why attestation belongs in the append-only record while rendering does not.

## same appearance, different world

Formally: visual equivalence $M \sim_R M'$ iff $R(M, \omega) = R(M',
\omega)$ for the relevant class of viewing conditions; historical
equivalence for a semantic task $H \equiv_T H'$ iff $T(\text{Fold}_S(H)) =
T(\text{Fold}_S(H'))$. In general

$$M_t \sim_R M'_t \;\not\Rightarrow\; H_t \equiv_T H'_t$$

A file recreated byte-for-byte after deletion looks identical yet may not
possess the same custody chain; an object placed at the same coordinates
may differ because one arrived through an admissible transition and the
other through an unauthorized rewrite; **a refusal can be materially silent
while semantically decisive**. The reverse separation also holds: a display
is a quotient, intentionally identifying histories its rule does not
distinguish — that becomes a defect only when a quotient optimized for
appearance is treated as sufficient evidence for identity.

## layering reconsidered — and jurisdictional drift

An abstraction boundary establishes a task-specific quotient and transfers
authority over a limited class of operations. The material fold is a
controlled reduction of committed history for operational use; rendering is
a further controlled reduction for appearance; the semantic fold runs
**alongside** — a provenance query and a frame render are not deeper and
shallower answers to one question but answers to different questions from a
common commitment base. The linkage is algebraic and evidential, checked by
replay, digests, version positions, or correspondence proofs (refinement
mappings in the Abadi–Lamport sense).

A second failure mode now appears beside technical debt: **jurisdictional
drift** — a material cache answering provenance questions; a renderer
becoming a commit mechanism; a semantic index treated as operational
state; a log placed on the critical path of disposable presentation. The
problem is not that a layer leaks but that one projection is asked to
exercise authority outside the task it was built for.

The desired invariant:

$$M_t = \text{Fold}_M(H_t; M_0), \quad S_t = \text{Fold}_S(H_t; S_0), \quad x_{t,\omega} = \text{Render}(M_t, \omega_t), \quad H_{t+1} = H_t \mathbin{\|} e_{t+1} \text{ only after a valid commitment}$$

The equations state logical relations; they leave open whether folds are
eager or lazy, centralized or distributed, cached in one structure or many.
What matters is that the **jurisdictions remain legible**.

---

## what this means for the engine

This paper is the engine's own architecture written back to it — every
equation has an existing, running implementation:

| Flyxion concept | the 8b-is engine |
|---|---|
| one log, two folds | `world-keep`: one append-only ledger, `Fold_M` (the zone state) and `Fold_S` (frontier, refusals, admissibility) — a refusal changes $S$ while $M$ stays put |
| $M_t = \text{Fold}_M(H_t; M_0)$ — legitimacy, not access | the keeper folds incrementally; replay is the **certification** (checkpoint validity), not the access pattern |
| $\text{Render}(M_t, \omega_t)$, never $H_{\le t}$ | the GAIA dashboard renders `gaia.state` (the material fold), never the ledger; the renderer cannot write history |
| Principle 2 (attestation boundary) | the mesh-NPC attests **pre-action needs** — the action is admitted only as an attested constraint on continuation; `nats_subscribe` (looking) commits nothing, `publish` (attesting) does |
| a refusal is materially silent, semantically decisive | the keeper's refusal leaves the zone unchanged and appends to `ledger.zone.refused` — the custody record, durable, never patched |
| $M \sim_R M' \not\Rightarrow H \equiv_T H'$ | two zones with identical state can differ in frontier and refusals; the engine adjudicates identity by the ledger, never by the render |
| snapshot reductionism vs log absolutism | the doctrine: the zone state never answers provenance (replay does); the ledger never sits on the render path |
| jurisdictional drift | the engine's named failure mode: the material cache (zone) must never become the semantic record, the dashboard must never become a commit mechanism |
| checkpoint validity | `--replay` re-folds from the seed and verifies $M$ matches — a checkpoint is trusted only when certified |
| attestation is not infallibility | later events can supersede an attested claim; the record keeps *that it was made* — the engine's refusals are exactly this shape |

And the wall, twice remembered (the Hadestown reading the constellation
already carries): Hades' "Why We Build the Wall" is the semantic fold used
as propaganda — the same stones are $M_t$ (what the wall physically is) and
$S_t$ (who built it, why, whether the fear was real); the song's circular
reasoning is a jurisdictional drift made musical: a material fold being
asked to answer a provenance question, and the workers' repetition is the
attestation that keeps the false fold alive. The engine's wall — the one in
the layers addendum — keeps the two memories in separate folds on purpose.

## the open questions

1. **Fold isomorphism**: when may $M$ and $S$ legally share a structure, and
   when must they diverge? The keeper keeps them separate today; the paper
   only says "may coincide for simple events."
2. **Attestation scope**: what belongs in the attestation record $a$
   (agent, method, scope) for the engine's actors — and what is the
   minimal attestation that still narrows $A_{t+1}$ usefully?
3. **Jurisdictional drift as a test**: can drift be detected mechanically —
   a lint over the mesh's subjects that flags any subject answering
   questions outside its fold's jurisdiction?
4. **Certification cost**: how cheap can checkpoint certification be made
   while staying a real proof, not a promise (digests vs full replay)?

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*
