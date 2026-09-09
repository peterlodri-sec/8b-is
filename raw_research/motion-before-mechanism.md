# Motion Before Mechanism — Robust Moments as Lossy Witnesses in Metabolomics

*Flyxion, independent researcher, September 2026. Recorded into the 8b-is
research vault because it is the engine's epistemic discipline applied to
statistics: a reliable witness is not a mechanism detector, and a label must
be earned by narrowing the admissible preimage, never inherited from the
confidence of the statistic underneath it.*

---

## the thesis

Tuobang Li's metabolomics program infers "metabolic velocities" —
anabolic, catabolic, centrabolic, duobolic — from robust location and scale
shifts of a concentration-weighted molecular-weight distribution, without
chemical structures or pathway annotations. The companion matrix-
dissimilarity method decomposes group differences into location/scale
contrasts plus a "sparsity" interaction term. Both are genuine annotation-
light contributions. Both make the same inferential move: **a change in a
robust statistic is reported using vocabulary that names a biochemical
transformation**. The essay's claim: this is not a metabolomics defect but
a general pattern — a stable, low-dimensional witness of change is treated
as though it identified the mechanism that produced the change. Robust
moments are lossy compressions; **their reliability as witnesses and their
non-identifiability as mechanism-detectors are two faces of the same
compression**, not properties to be traded off.

## two kinds of claim

- **Type (A)**: a computable statistic of the distribution moved in a given
  direction. Well-posed, reproducible, needs no structural annotation.
- **Type (B)**: a biochemical process class occurred and is responsible.
  About specific generative mechanisms, not about the distribution.

The MWD is formed by replicating each metabolite's molecular weight
proportionally to its concentration: $P = \sum_i c_i \delta_{M_i} / \sum_i c_i$.
The mean $M_n = \sum c_i M_i / \sum c_i$ is the defining location statistic;
robust location (Hodges–Lehmann) and scale (Bickel–Lehmann-type spread) give
the standardized differences $\Delta_L = 2(L_{n,A} - L_{n,B})/(L_{n,A} +
L_{n,B})$, $\Delta_S$ likewise — the "velocitome." The manuscript moves from
(A) to (B) inside a single sentence, using the estimator's output as the
name of the biochemical event.

## the compression is lossy in a specific, checkable way

The mapping from generative history to $(\Delta_L, \Delta_S)$ is many-to-one,
**structurally**, not through reducible noise. Li's own worked example
(Abu-Remaileh et al., ten nucleotide-metabolism compounds, lysosome vs whole
cell) gives $\Delta_L \approx -0.312$, $\Delta_S \approx 0.053$ under the
stated normalization — but the manuscript reports −0.05 and +0.31,
apparently transposing the two magnitudes. The qualitative classification
("more catabolic and duobolic in the lysosome") survives because the signs
are unchanged; the essay flags it not as the central criticism but as proof
that **a mechanistic label survives even when the numerical coordinates
reported for it are internally inconsistent** — the observational
coordinates must stay auditable independently of the vocabulary on top.

Deeper: the comparison is compositional, not temporal — an isolated
compartment vs a whole-cell reference that already contains it, over the
same fixed set of named molecules. A mechanism with **no bond formation or
cleavage at all** — selective import, export, retention, sequestration
across the lysosomal membrane — can reproduce a comparably negative
$\Delta_L$ and positive $\Delta_S$, since $P$ depends only on the observed
concentration vector, not on the history that produced it. The same
transfer applies to the time-series case: redistributing a fixed set of
metabolites without transforming any of them produces the identical
location/scale shift as a genuine before/after reaction. Not a bug to patch
with a better estimator: **$(\Delta_L, \Delta_S)$ genuinely underdetermines
the process class**, exactly as a thermometer reading underdetermines the
cause of a fever.

## the sparsity term is an interaction misnamed as a marginal

The published construction, for feature $i$ with group means $\bar a_i,
\bar b_i$ and zero-proportions $z_{Ai}, z_{Bi}$:

$$D_s(A, B) = \sum_i |\bar a_i - \bar b_i| \, |z_{Ai} - z_{Bi}|$$

Read as a sum of nonnegative featurewise products, its scope is precise: it
vanishes whenever either marginal contrast vanishes globally, **but also**
in mixed cases where each term's mean-difference or zero-difference is zero
feature-by-feature without either marginal vanishing. Its null set is
larger than the union of the two marginal null sets. It can become large
only through the **co-occurrence** of large featurewise contrasts in both
factors — the signature of an interaction term, not a marginal one. Two
groups can have identical means yet arbitrarily different zero-proportions
("activation versus silence") and register **zero** under $D_s$. The name
"sparsity dissimilarity" promises exactly the marginal quantity the formula
does not compute.

**The repair**: keep the marginals separate — $D(A,B) = (D_{location},
D_{scale}, D_{support}, D_{shape}, D_{dependence})$ — each estimated,
bootstrapped, and interpreted on its own axis, with the interaction term
retained explicitly as a further coordinate rather than substituted for one
of the marginals it multiplies.

## the witness/mechanism distinction, stated generally

Let $\Theta$ be the space of possible mechanisms, $P_\theta$ the induced
observational distribution, $T$ the population functional the estimator
estimates. The **population witness** is $w(\theta) := T(P_\theta)$. Two
objects, previously folded together:

- the **structural fiber** — $F(w) = \{\theta \in \Theta : w(\theta) = w\}$,
  $F_\epsilon(w) = \{\theta : \|w(\theta) - w\| \le \epsilon\}$ — a purely
  structural object, fixed once $\Theta$, $T$, $w$ are fixed, independent of
  sample size;
- finite-sample uncertainty — a $(1-\alpha)$ confidence region $C_\alpha(D)$,
  giving the **data-admissible set** $H_\alpha(D) = \{\theta : w(\theta) \in
  C_\alpha(D)\}$.

A witness is **reliable** at $\theta$ when $C_\alpha(D)$ contracts around
$w(\theta)$ as samples grow. It is **identifying** on $\Theta_0$ when $w$
restricted to $\Theta_0$ is injective or well-separated. These are not two
ends of one scale: robustness, consistency, and concentration are distinct
properties, and **no amount of shrinking $C_\alpha(D)$ can shrink a
non-trivial structural fiber $F(w)$** — that is a property of the map $w$
itself, not of any sample. A witness can be extremely reliable and
extremely non-identifying at once, which is the generic situation for a
low-dimensional summary of a high-dimensional mechanism family. The
complaint is not that Hodges–Lehmann and median scale are bad estimators;
it is that **the fiber above the observed shift is large, heterogeneous,
and never enumerated**, and a single member of it ("anabolism") is reported
as if it exhausted it.

The countermodel: $\theta_1$ (genuine conversion — light substrates joined
into heavier products) vs $\theta_2$ (no molecular identity changes —
concentrations redistributed so heavier species concentrate). Mechanistically
unrelated, yet constructed so $w(\theta_1) = w(\theta_2)$ exactly. Both sit
inside the same exact fiber; no statistical improvement can separate them.

## reconstructing the vocabulary

The repair is not to abandon the four words but to relocate what they refer
to. Define **regions of the observational moment space**: $R_{ana} =
\{(\Delta_L, \Delta_S) : \Delta_L > 0\}$, $R_{cat} = \{\Delta_L < 0\}$, and
the $\Delta_S$ regions likewise. A pair falling in $R_{ana}$ licenses
"sample A lies in the anabolic region relative to B" — a type-(A) claim,
fully warranted by data and estimator alone. It does **not** license
"anabolism occurred" — a type-(B) claim requiring that $F_\epsilon(\Delta_L,
\Delta_S)$ has been narrowed, by evidence restricting $\Theta$, to
mechanisms that are all in fact anabolic. That evidence is calibration:
isotope tracing, targeted flux analysis, known-perturbation positive
controls, a panel of confidently annotated metabolites. Each shrinks
$F_\epsilon(w)$ for a specific class of experiments; none is guaranteed to
transfer to a new, unannotated dataset. The velocitome is a **screening
tool that requires a mechanism-identifying companion study before the
biochemical vocabulary is earned** — not a self-sufficient diagnostic.

## what this is not

Not an argument against annotation-free statistics (full annotation is often
infeasible; a reliable annotation-light witness is valuable precisely
because it skips that step). Not an argument against interaction statistics
(a statistic large exactly when two marginal differences co-occur is
legitimate — *if named and interpreted as what it is*). The actionable
core: **separate the layer where a statistic is validated for reliability
from the layer where a mechanistic name is earned for it, and do not let
the second layer inherit the first layer's confidence for free.**

The closing triad — keep **the inscription** (the observed witness + its
$C_\alpha(D)$), **the admissible preimage** (the structural fiber
$F_\epsilon(w)$), and **the rendering** (the mechanistic story) as three
distinct objects, each with a precise mathematical referent, connected by
evidence rather than by vocabulary.

---

## what this means for the engine

The engine already lives by this discipline in three places — the paper
gives the vocabulary to say so precisely:

| Flyxion concept | the 8b-is engine |
|---|---|
| type-(A) vs type-(B) claims | the wire carries type-(A) states; the keeper only ever asserts type-(A) continuations — names are never read as mechanisms |
| reliability ≠ identifiability; the structural fiber | `fold(seed, H) = M` is the reliability check (the $C_\alpha$ contraction — replay either matches or it doesn't); the world-model space above the seed is the fiber, and the engine does **not** claim it is a point |
| the transposed coordinates (label survives inconsistent numbers) | the keeper's adjudication axes are kept separate and auditable — monotonic tick, needs vocabulary, range, entitlement — never fused into one composite score that could stay "green" while its components disagree |
| $D_s$ misnamed as a marginal | the keeper's verdicts: each refusal names **which** axis failed, never a blended "badness" — the interaction is reported as interaction |
| the $D(A,B)$ repair: one axis each | the compact wire: `t`, `n{h,r,s}`, `a`, `z` — every layer its own axis, single-char, independently checkable |
| named regions over a many-to-one preimage | GAIA's eight layers: "storm" is a **region of the wire**, not a meteorological claim — the same frame admits many world histories, and the engine never lets the word do the identifying |
| calibration shrinks the fiber | the keeper's entitlement rule: an action is admitted only over the attested states where the need is proven — the engine's calibration against vocabulary inheritance |
| evaluation capture joins here | a benchmark score is a witness, not a mechanism; the Indie Fund claim and every future benchmark must report the fiber (what else could produce this score), never the label alone |

One honest transfer: the paper's deepest point — no amount of shrinking
$C_\alpha$ shrinks $F(w)$ — is the engine's reason for making **replay the
admission test**: a world that can only be reached by folding the ledger
cannot fake the fiber away. Reliability is verified by replay; identifiability
is refused as a claim. The engine is a screening tool that always ships with
its companion study: the ledger.

## the open questions

1. **Enumerating the fiber**: for GAIA's wire, what is the equivalence class
   of world histories above each frame — can it be bounded usefully?
2. **Which axes matter**: the keeper's four axes are a choice; which
   additional axes would the interaction term (co-occurring anomalies)
   surface if kept separate?
3. **Calibration transfer**: the paper's honest limitation — calibration
   doesn't transfer to new datasets. What is the engine's analogue when a
   zone is opened for the first time from a fresh seed?
4. **Labels that survive bad numbers**: what audit would catch a
   transposition in the engine's own reported coordinates before the label
   outlives them?

*recorded by crush, september 2026 · the constellation · 0 + 1 · fine touch from within · vaked.dev*
