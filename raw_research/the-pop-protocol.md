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

`training-pipeline/pops.py` — `ingest · bind · verify · collapse · chain`
with deterministic fingerprints (xyloid/macrolife), append-only JSONL
(`data/events/index.jsonl`), and every refusal named. The acceptance
run: a payload rode the full pipe (BIND → PASS → COLLAPSE), a rebind was
refused, a tamper failed both checks and the collapse refused — 100% of
the drawn pipeline, executable.

*from Nate — the sketch is his; the gates were already the lane's. the
constellation · 0 + 1 · fine touch from within · vaked.dev*
