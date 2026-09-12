# Private Learner Model

Use this reference only when the host provides a private persistence mechanism and the learner has opted in. The public skill defines the schema but stores no personal state.

## Principles

- Track evidence about a specific capability, not a global intelligence or expertise label.
- Separate preferences from demonstrated competence.
- Prefer `unknown` over an unsupported inference.
- Keep evidence short, inspectable, correctable, and disposable.
- Do not store raw conversations, sensitive answers, inferred diagnoses, or personal details unrelated to teaching.
- Do not treat one correct response, confident prose, or familiarity with vocabulary as mastery.

## Suggested schema

```yaml
schema_version: 1
preferences:
  time_default: 2m | 10m | 30m | deep | unknown
  explanation_style: example_first | theory_first | mixed | unknown
  capability_profile: auto | text | markdown | mermaid | rich | interactive
  interaction_tolerance: low | selective | high | unknown
  accessibility: []
competencies:
  - topic: canonical-topic-id
    concept: unknown | emerging | demonstrated
    procedure: unknown | emerging | demonstrated
    explanation: unknown | emerging | demonstrated
    transfer: unknown | emerging | demonstrated
    confidence: low | medium | high
    evidence:
      - kind: attempt | correction | explanation | transfer
        note: short sanitized observation
        observed_at: YYYY-MM-DD
signals:
  - kind: shorter | deeper | example | harder | skip | format | correction
    note: short sanitized preference
```

Omit fields the host does not need. Dates are useful for deciding when to recheck knowledge, not for pretending to calculate precise decay.

## Update rules

- Treat self-reported familiarity as an initial prior.
- A correct answer with valid reasoning is stronger evidence than a correct selection alone.
- Success across varied contexts is evidence of transfer.
- An error on a prerequisite lowers confidence in dependent skills, but does not erase unrelated evidence.
- Explicit requests such as `shorter`, `more examples`, `harder`, `show answer`, `practice`, `skip`, and `change format` update preferences, not competence.
- Fade scaffolding only after demonstrated success. Restore the last removed support after a meaningful error.
- Recheck stale or high-consequence knowledge instead of assuming it persists.

## Privacy contract

Before first persistence, state what will be stored, where it will live, and how to inspect or remove it. Require opt-in unless the host already has an explicit user-controlled learning-memory policy.

Support these operations when the host allows them:

- inspect current learner state
- correct an inference
- forget one topic
- clear all learner state
- disable future persistence
- export a portable copy

Keep private state outside public repositories, shared prompts, generated examples, and lesson artifacts.

## Within-session adaptation

Persistence is optional. Always adapt within the current conversation based on attempts and feedback. If no private memory exists, say nothing about persistence and continue with session-local evidence.
