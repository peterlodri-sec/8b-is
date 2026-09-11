# the POP protocol (from Nate :)

*Nate's sketch, absorbed into the lane's record layer: an event is five
fields bound by a content hash, and a pipeline that can only go forward —
POP → REFUSE → BIND → transform → verification bound → COLLAPSE → ledger.*

## the envelope

| field | the lane's meaning |
|---|---|
| event_id | sha256(source\|content_hash)[:16] — the monotonic key |
| timestamp | UTC, at the POP |
| content_hash | sha256 of the payload bytes, bound at ingress |
| source | who/what sent it (named, always) |
| payload_reference | the path/HF ref the payload lives at |

## the pipeline, mapped to what we already had

| POP | the constellation's echo |
|---|---|
| ingress / POP | the oven's ingestion point — nothing enters unnamed |
| admissibility / REFUSE | the stage machine's named refusals + the accelerator gate that never lies |
| binder / BIND | run.json + the model card: the manifest binds the artifact |
| transformation A (xyloid) · B (macrolife) | the twin transforms — one event, one bound transform, fingerprints over the payload |
| verifier / verification bound | the golden's discipline: re-derive, compare, never trust the record |
| COLLAPSE / committed outcome | the stage machine's one-step commit — only verified states collapse |
| ledger / history · residuals | the monotonic events index + runs.parquet + .lane-state |

## the code

`training-pipeline/pops.py` — the protocol KERNEL (Nate's robustness set,
v2): records carry `id · kind · parent · payload_hash · payload_ref ·
timestamp · actor · protocol_version · attestation`; the ledger is hash-
linked (`hash(prev || cur)`, the head commits the whole history); lanes
are monotonic lineages (multiple lanes per log, no branching); REFUSE is
a record — a refused event is historically visible, never "nothing
happened". The interface stays narrow and pure:

    append(record) · verify_record · verify_transition
    verify_lane = V_schema ∧ V_transition ∧ V_references
                  ∧ V_hash-chain ∧ V_monotonicity ∧ V_no-branching
    admissible_transition(a, b) · replay · head

Determinism contract honored: same records + same protocol version =
same verification result — no network, no payload mutation, no corridor
names. The acceptance: a full lane (POP→BIND→TRANSFORM×2→VERIFY→COLLAPSE)
plus a refused lane and an open lane — V(L) all True over the 3-lane
history; a tampered attestation flips hash_chain+transition and the
collapse refuses; reopening a refused lane by rebinding is refused at
append. The divider stands: corridor code produces events, pops.py
verifies their admissible succession, the ledger preserves, semantic
verifiers judge domain claims, COLLAPSE records which verified candidate
became operative.

*from Nate — the sketch is his; the gates were already the lane's. the
constellation · 0 + 1 · fine touch from within · vaked.dev*
