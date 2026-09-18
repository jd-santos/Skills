---
name: technical-writing
description: Writes and edits accurate technical documentation, explanations, guides, references, specs, and agent instructions. Use with core-writing when technical content needs clear structure, preserved operational detail, or adaptation to a technical audience.
version: 1.0.0
author: jdwork
category: documentation
requires: [core-writing]
---

# Technical Writing

Apply `core-writing` first. This skill adds rules for technical accuracy, document structure, and operational usefulness.

## Establish the technical context

Before drafting or rewriting, determine:

- **Audience:** users, contributors, maintainers, operators, or AI agents
- **Purpose:** quick start, tutorial, reference, explanation, troubleshooting, spec, or proposal
- **Expected knowledge:** what can be assumed and what needs definition
- **Source of truth:** code, configuration, tests, project docs, or cited external material

Match an existing project's terminology and useful conventions. Correct a weak local style only when that is part of the task.

## Protect technical meaning

- Preserve commands, paths, configuration keys, code samples, constraints, and warnings that affect outcomes.
- Verify technical claims when the source is available. Mark uncertainty instead of filling gaps.
- Use one term for each concept unless the distinction matters.
- Define unfamiliar terms near first use. Do not define routine terms for an expert audience.
- Explain why when it affects a decision, tradeoff, failure mode, or maintenance burden.
- Separate requirements from recommendations and current behavior from proposed behavior.

## Fit the document type

- **Quick starts:** Give prerequisites, the shortest working path, and a way to verify success.
- **Tutorials:** Use a runnable sequence and explain the important causal links.
- **Reference docs:** Favor predictable headings, exact syntax, defaults, edge cases, and examples.
- **Troubleshooting:** Organize around symptoms, checks, likely causes, and fixes.
- **Specs and proposals:** State the problem, constraints, decision, tradeoffs, and open questions.
- **Agent instructions:** Use explicit, imperative language. Precision matters more than conversational warmth.

## Use examples deliberately

Keep examples minimal enough to understand but complete enough to use. Label placeholders, expected output, destructive commands, and environment-specific assumptions. Do not add examples that merely repeat the prose.

## Edit existing technical material

Read surrounding documentation before changing its voice or structure. Preserve useful detail even when tightening the prose. Do not remove setup steps, failure cases, diagrams, or caveats solely to make the document shorter.

## Example

Instead of:

> It is recommended that users ensure the configuration file has been created prior to initiating the application.

Write:

> Create the configuration file before starting the application.

Add the path, command, or verification step when the reader needs it to act.
