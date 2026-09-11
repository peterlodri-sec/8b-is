# the POP protocol (from Nate :)

*Nate's sketch, absorbed into the lane's record layer: an event is five
fields bound by a content hash, and a pipeline that can only go forward —
POP → REFUSE → BIND → transform → verification bound → COLLAPSE → ledger.*

## the envelope

| field | the lane's meaning |
|---|---|
| event_id | `sha256(source \|\| payload_hash)[:16]` — the **stable event key**, content-derived; the timestamp and ledger position carry the monotonic order, never this id |
| timestamp | UTC, at the POP — the monotonic order lives HERE |
| payload_hash | `sha256(payload_bytes)` — the hash binds the payload |
| payload_reference | the path/HF ref the payload lives at |
| source | who/what sent it (named, always) |

The ledger chain binds the event **records** themselves
(`attestation = sha256(prev \|\| cur)`); the head commits the whole
history.

## one sentence

> POP establishes identity, REFUSE establishes admissibility, BIND
> establishes relation, transforms propose outcomes, VERIFY re-derives
> warrant, COLLAPSE makes one verified outcome operative, and the ledger
> preserves both the path taken and the paths refused.

The last clause is where the lane stops being a conventional CI pipeline:
residuals and named refusals are preserved as records, not erased.

## the city is running

The distributed expression is alive on bonobo@Memex: eight containers
on flyxion/alpine-minimal (`spherepop-pop · refuse · bind · xyloid ·
macrolife · verify · collapse · ledger`). The treaty is written:
`training-pipeline/pops.contract.json` (the nine-field record schema,
kernel-validated) and `docs/spherepop-contract.md` (the container → kind
map + the machinery table). Lane kernel and the city speak the same records; the contract is
the boundary. **Cross-parity closed**: the Go city's event ids match
the canonical `sha256(source | payload_hash)[:16]` bit-exactly on two
live samples — the single-pipe derivation won, the kernel converged.

## two expressions, one deep grammar

The same protocol has two honest embeddings. The LANE/embedded style:
one machine, one pipeline, logical boundaries, shared memory, trust by
structure, failure is a path, replay the program, code defines the
boundaries. The SERVICE/distributed style: a small city, physical +
networked boundaries, explicit records, distrust by default, failure is
a place (timeout → circuit open; retry → alternate executor; residual →
preserved evidence), replay the history, contracts define the
boundaries. The grammar both preserve:

```
something appears → POP → may it proceed? → REFUSE → what is it bound
to? → BIND → produce a candidate → TRANSFORM → does it warrant
acceptance? → VERIFY → make one outcome operative → COLLAPSE → do not
erase how we got there → LEDGER
```

`pops.py` is the lane's side of that grammar, kept narrow on purpose:
the protocol kernel verifies the succession, the corridor supplies the
transforms and semantic verifiers, the ledger preserves, and (in the
service style) the same records become the space between programs.

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
