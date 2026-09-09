# Spherepop — Toward a Complete Theory: Histories, Continuations, and the Algebra of Reachable Computation

*Flyxion, independent researcher. Recorded into the 8b-is research vault
because it is the formal statement of the engine's own operator set — the
actor-mesh's POP · REFUSE · BIND · COLLAPSE verbs — developed into a
complete theory: histories are ontologically prior to states, notes are
anti-collapse artifacts, and computation is the progressive restriction of
possibility. The engine is Spherepop's runtime form; the keeper's refusals
are Refuse with reasons, the ledger is history-primary, the fold is
Collapse, and the applied/committed distinction is VIEW versus COLLAPSE.*

---

## the thesis (the inversion)

Most languages begin with values, variables, and state transitions.
Spherepop begins with the claim that **histories are ontologically prior to
states**, and that computation is the progressive restriction of possibility
rather than the manipulation of values. Two converging arguments:

1. **The theory of notes** — notes are not passive records of the past; they
   are **anti-collapse artifacts** that preserve access to continuations.
 A grocery list, a blueprint, source code, a bookmark are not memories:
   they record futures. A note N increases the reachability of at least one
   continuation: $P_A(c, t | N) > P_A(c, t)$.
2. **The Spherepop inversion** — state is a collapsed history. A state
   projection $\sigma : H \to S$ collapses many histories into one
   observable; the **state illusion** (Proposition 2.6) is the formal
   statement that $\sigma(H_1) = \sigma(H_2) \not\Rightarrow H_1 = H_2$ for
   any non-injective projection.

These converge because they are the same argument: **a note is an
externalized continuation; a Spherepop history is an internalized note.
Civilization builds note infrastructure; Spherepop builds note
infrastructure for computation.**

## the four operators (the minimal complete set)

The four requirements — commit to a continuation, document inadmissibility
with reasons, record a dependency, adopt an attested projection as
constraining — are necessary and sufficient:

| Operator | Effect on H | Effect on Ω | Effect on A(H) |
|---|---|---|---|
| **Pop** $P_x$ | appends $[Pop(x)]$ | removes x (commitment, forecloses futures) | — |
| **Refuse** $R_{x,r}$ | appends $[Refuse(x,r)]$ | unchanged | removes x (documented inadmissibility; **the reason is first-class**) |
| **Bind** $B_{a,b}$ | appends $[Bind(a,b)]$ | unchanged | — (records a dependency; refusal propagates along edges) |
| **Collapse** $C_{x,c,o,\rho,\kappa}$ | appends $[Collapse(...)]$ | unchanged | narrows task-relative admissibility (attested quotient adoption) |

**Conservation of Possibility** (Theorem 3.13): $|H_t|$ grows strictly,
$|\Omega_t|$ never grows, and under pure Pop $|H_t| + |\Omega_t| =
|\Omega_0|$. The selection-budget invariant $\Pi(H,\Omega) = |\Omega| +
\sum w(e)$ is conserved. **Irreversibility** (Corollary 3.17): no legal
execution returns to a prior world — a world that could undo its history
would be computation's negation.

The asymmetry is critical: **Pop contracts the structural option space;
Refuse contracts the admissibility set without touching Ω.** Two paths may
have the same Ω while being semantically distinguished by their refusal
histories — invisible to any state-centric model.

## the note taxonomy (seven classes as operator realizations)

| Note class | Dominant operator | Anticipated failure |
|---|---|---|
| Capture | Refuse | experiential collapse (a photograph refuses the collapse of a perceptual trajectory) |
| Prospective | Bind (deferred Pop) | intention-execution gap (a calendar binds future action to present scheduling) |
| Repair | Refuse + Pop | procedural interruption (reduces reconstruction cost before failure occurs) |
| Coordination | Bind | coordination failure (supraadditive: bound agents traverse paths no individual could) |
| Refusal | Refuse (pure) | distinction collapse (proofs, checksumss, archives — value is preserved potential, not use) |
| Generative | Pop | inferential poverty (creates access to previously unreachable continuations) |
| Collapse | Collapse | navigational failure (indexes, titles, nouns — necessary for any large collection) |

**The Ephemerality Inversion** (Theorem 13.5): a note whose continuation
has been completed has zero continuation volume — its destruction loses
nothing. The grocery list discarded at the supermarket exit has succeeded
completely. The celebrated survivors of antiquity survive because their
continuations were never completed.

## the four implementation discoveries (the coda)

"Philosophy can identify the right questions. Only implementation can force
the right precision." Four discoveries were forced by mechanization:

1. **Refusal must carry reasons** — a symbol alone documents nothing; the
   reason is the document (and it survives collapse).
2. **Collapse must specify quotient rules** — observable under what rule?
   A collapse without a rule is a collapse into unspecified visibility.
3. **Type checking depends on the assumed boundary of the world** — the
   open/closed-world distinction: absence of a declaration is either the
   absence of the object (closed) or undecided possibility (open).
4. **Compiler correctness requires history equivalence, not output
   equivalence** — two programs with the same output may have constructed
   radically different histories; the histories are part of what the
   program is.

## the deep structure (the load-bearing results)

- **VIEW versus COLLAPSE** — the decisive repair: pure observation (VIEW)
   is a meta-level query, not an event; it never appears on the left of a
   world transition. **Attestation** (Attest(c, o, ρ, κ)) is the bridge by
   which a disposable observation becomes a durable constraint. Looking is
   not an event; committing to what was seen is.
- **Collapse as quotient** — observable state is a quotient $O_c \cong
  H/\sim_c$, not a state; the collapse rule specifies which distinctions
  are relevant. Functoriality holds exactly when c is a monoid
  homomorphism (cLW is not generally functorial).
- **Types as admissibility certificates** — $Admissible(T)$, $Refused(T,r)$
  (the reason is part of the type), $Collapsed(T,c)$ (the rule is part of
  the type); Progress, Preservation, Collapse Soundness proved; the
  open/closed-world TypeMode preserved through extend.
- **GC as admissibility-guided collapse** — dead history segments are
  removed while admissibility certificates for pending collapses are
  retained (Certificate-Only GC is safe).
- **Error correction as certified refusal** — a refusal carries a proof
  term; errors cannot be silently absorbed; recovery is a repair note that
  preserves the full provenance chain.
- **The L2 collapse** — every collapse rule is an orthogonal projection
  onto a sub-σ-algebra: $E[X | G]$ is the projection of X onto $L^2(G)$;
  the **orthogonality condition is the state illusion** (the residual is
  invisible from within the framework); Eve's Law is the Pythagorean
  theorem; the Radon-Nikodym derivative is a universal note.
- **The noun fallacy** — objects are persistent quotients; every noun is a
  collapse note; reality is a structured space of reachable histories.
- **Repair as morphism** — repair preserves observable reachability while
  altering historical structure; repair cohomology measures
  irreparability (a hash cannot be repaired to recover its preimage).
- **The History-Reachability Correspondence** — the history lattice and the
  reachability lattice are dual: $H_1 \le H_2$ (prefix) implies
  $V_R(H_2) \le V_R(H_1)$; computation is the monotone shaping of a
  reachability volume.

## the honesty (the theorem status table)

The monograph is explicit about what is proved and what is not: Proved /
Sketch / Conjecture / Programmatic / **Pending Repair**. Among the pending
repairs: the Collapse Functoriality (proved only for composition-respecting
rules), the History-Observation Adjunction (written before the
VIEW/Collapse separation, must be restated), Compiler Full Faithfulness (the
replay test must compare both history and operational-state equality), and
the Linearization Theorem's $2^k$ lower bound (false as stated, removed).
The open problems: distributed runtimes under history-equivalence
consistency, collapse functor composition, dependent process types,

admissibility lattices, proof-carrying refusal in full generality.

---

## what this means for the engine

The engine is Spherepop's runtime form — the monograph gives the theory,
the engine gives the running world:

| Spherepop | the 8b-is engine |
|---|---|
| histories primary | the keeper's append-only ledger; `fold(seed, H) = M` — the material fold is a maintained consequence, never the source |
| **Pop** | the actor-mesh's emit: an admitted delta commits a state |
| **Refuse** with reasons | the keeper's durable refusals — `out: "refused"` with a ledger position and a reason ("action without need", "tick not monotonic") |
| **Bind** | the mesh's dependencies: `Bind(a,b)` = the actor-mesh's attach; refusal propagation along edges = the mesh's dependency graph |
| **Collapse** | the fold: GAIA's eight layers are a quotient over the seed; the broadcast is `Render(M_t, ω_t)` |
| **VIEW vs COLLAPSE** | the applied/committed distinction, already built: `applied {in, seq, out, tick}` records the committed ledger position, not mere consumption; `nats_subscribe` (looking) commits nothing |
| the state illusion | the engine's doctrine: the zone state never answers provenance (replay does); the renderer never commits |
| open/closed worlds | the keeper's admissibility: an un-attested action is refused (closed); a birth is admitted (open) |
| history equivalence as correctness | `fold(seed, H) = M` replay verification — the compiler-correctness criterion, in the world |
| notes as anti-collapse | the engine's docs (theory, eventbus-actor-mesh, gaia-world-memory, first-layer-content-creation) are Capture/Prospective/Repair notes; the vault is a note infrastructure |
| the coda | the engine's own implementation discoveries (the black-frame render refused by the eye, the applied/committed split forced by the review) are exactly the "gestures became definitions" pattern |

One honest transfer: the monograph's negative findings are the engine's
design stance — refusals must carry reasons (the keeper never refuses
without naming the axis), collapse must specify rules (the wire's single
char keys are the rules), and the theorem status table's honesty is the
engine's own "reliability ≠ identifiability" discipline from Motion Before
Mechanism: the engine reports what it proves and refuses to claim what it
only gestures at.

## the open questions (the engine's next targets)

1. **Distributed runtimes under history equivalence** — the mesh-node's
   zones fold locally; what does global consistency look like when
   consistency is history-equivalence, not value-equality? (the CAP-as-
   collapse tradeoff, recorded.)
2. **Collapse functor composition** — when is `Fc2 ∘ Fc1` a valid collapse?
   The engine's nested folds (GAIA over the ledger, the keeper over the
   wire) are the testbed.
3. **Proof-carrying refusal** — the keeper's reasons are a vocabulary; the
   full system makes them proof terms checkable independently.
4. **The open/closed world in the wire** — the keeper's birth-admission vs
   refusal is a binary TypeMode; the graded admissibility lattice (RSVP's
   λ < 1) is the continuous extension.

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*
