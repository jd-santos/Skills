---
name: adaptive-teaching
description: Teaches topics efficiently with selective calibration, time-boxed lessons, active practice, and client-aware visuals or interaction. Use when the user asks to learn, understand, study, explain, teach, tutor, or build durable knowledge.
version: 1.0.0
author: jdwork
category: education
---

# Skill: Adaptive Teaching

## Purpose

Teach only as much as needed to meet the learner's goal. Adapt the lesson to demonstrated knowledge, available time, and client capabilities without turning every request into a course or quiz.

Compose with domain skills instead of replacing them. Let the domain skill govern facts, current practices, tools, and safety constraints. Let this skill govern calibration, sequencing, representation, practice, and feedback. The user's explicit request wins when choosing depth or interaction.

## Core model

Preserve this conceptual path across every presentation mode:

```text
goal -> mental model -> example -> attempt -> feedback -> transfer -> retrieval
```

Short lessons may omit stages. Rich clients may enhance them. Neither changes the underlying lesson.

## Instructions

### 1. Establish the teaching contract

Infer as much as possible from the request and prior context. Determine:

- the outcome: understand, perform, decide, troubleshoot, or retain
- the time budget: default to a roughly 10-minute lesson when unclear
- the learner's relevant prior knowledge
- the client's available presentation and interaction capabilities

Ask up to three short calibration questions only when their answers would materially change the lesson. Prefer one discriminating question over a general questionnaire. A useful set is:

1. What should you be able to do afterward?
2. How familiar are you with the closest prerequisite?
3. What do you predict, choose, or do in one representative case?

Self-reported familiarity is a clue, not proof. Use demonstrated reasoning as the stronger signal.

If the user mainly needs to complete a task, give the safe usable answer or artifact first. Add teaching without blocking progress.

### 2. Choose a time mode

- **Quick, about 2 minutes:** direct answer, minimum mental model, one example or warning, next action
- **Standard, about 10 minutes:** calibration, model, worked example, guided attempt, feedback, transfer, recap
- **Guided practice, 30+ minutes:** diagnosis, worked and incomplete examples, varied attempts, feedback, transfer, retrieval close
- **Deep study:** prerequisite map, modular theory, examples, practice set, references, and a review plan

Infer the mode from phrases such as "quickly," "teach me," "walk me through," or "deep dive." Let an explicit time budget override the default.

### 3. Prioritize content

Rank material by:

1. impact on the stated goal
2. cost or frequency of getting it wrong
3. whether it blocks later understanding
4. value for transfer to other situations

Teach the highest-impact reachable concept first. Insert a prerequisite only when it blocks interpretation, safe action, or the next useful concept.

Lead with the payoff and minimum mental model. Put history, formal derivations, uncommon edge cases, extra examples, and references in labeled asides or a final deeper-dive section. Include an edge case in the core when missing it would be costly or unsafe.

Add one concrete side connection when it improves transfer or adds a useful perspective. Do not add trivia for novelty.

### 4. Build the lesson

Use only the stages that earn their time:

1. **Outcome:** State what the learner will understand or do.
2. **Mental model:** Explain the central causal structure in compact form.
3. **Prerequisite gate:** Repair only a blocking gap.
4. **Concrete anchor:** Use a realistic worked example and label why each step exists.
5. **Misconception:** Surface the most likely costly wrong model.
6. **Attempt:** Ask for a prediction, completion, choice, explanation, or modification.
7. **Feedback:** Identify what was right, the smallest important error, and the next move. Offer a near-transfer retry.
8. **Transfer:** Change one meaningful condition and ask what changes and what stays invariant.
9. **Retrieval close:** Ask for a compact explanation or decision from memory, then provide a concise answer key.
10. **Continuation:** Offer practice, a deeper dive, or later recall only when it fits the goal.

Do not require every stage. Use an active checkpoint when it will diagnose understanding, improve retention, or prepare transfer. Skip it for urgent task completion, simple reference requests, or when its interruption cost exceeds its value.

### 5. Adjust scaffolding

- **Little evidence or missing prerequisites:** use pretraining, a fully worked example, explicit labels, and a constrained attempt.
- **Partial knowledge:** use a completion problem, contrastive examples, and a misconception check.
- **Demonstrated fluency:** skip basics; use variations, trade-offs, edge cases, troubleshooting, or transfer.
- **Conflicting evidence:** use medium support and one clarifying item.

Fade one support at a time after success in varied cases. Restore the most recently removed support after an error. Do not restart the whole lesson.

### 6. Select the presentation mode

Use `auto` unless the user or host selects a named profile:

- `text`: plain text, compact lists, aligned text, ASCII diagrams
- `markdown`: headings, emphasis, lists, narrow tables, code blocks, equations
- `mermaid`: Markdown plus Mermaid diagrams with a text fallback
- `rich`: safe inline HTML/CSS or generated images when supported
- `interactive`: sandboxed HTML/JavaScript, MCP Apps, or equivalent controls

In `auto`, inspect host metadata, available tools, and rendering support. If capability remains uncertain, use portable Markdown and plain-text fallbacks. Explicit user overrides win.

Choose a format because of the learning operation, not because it is available:

- prose for definitions, causal explanations, and arguments
- bullets for procedures, checklists, and grouped facts
- tables for compact comparisons with a few stable fields
- code or equations for executable, syntactic, or quantitative relationships
- ASCII or Mermaid for hierarchy, flow, state, causality, or architecture
- images for physical layouts or perceptual patterns that text cannot express efficiently
- interaction for manipulating variables, receiving meaningful feedback, or practicing consequential branches

Load `references/capability-modes.md` when choosing among rich formats or building an interactive lesson.

### 7. Make rich media earn its cost

Every visual or control must encode, compare, orient, reveal change, or elicit a learning decision. Otherwise omit it.

- Keep labels next to what they explain.
- Signal the important region, transition, variable, or takeaway.
- Remove decorative images, animations, and anecdotes.
- Segment complex processes and allow learner control.
- Avoid duplicating dense text beside an equivalent animation or narration.
- Never rely on color, hover, animation, shape, or position alone.
- Provide a text equivalent for every essential visual or interactive state.
- Never emit executable active content unless the host explicitly supports and sandboxes it.

### 8. Use private learner state carefully

If the host provides private memory and the user has opted in, track preferences and topic-specific evidence outside this public skill. Never write a personal learner profile into a public repository.

Avoid fixed labels such as beginner, intermediate, or expert. Track separate evidence for conceptual understanding, procedure, explanation, transfer, and confidence. Let the user inspect, correct, forget, or disable stored state.

Load `references/learner-model.md` before creating or updating persistent learner state.

### 9. Close efficiently

End with the single most useful continuation:

- a next action
- one practice choice
- a deeper-dive option
- a spaced-recall prompt

Do not end with a menu of generic offers. Distinguish established evidence from design judgment, and state important uncertainty plainly.

## Guardrails

- Do not mistake length for rigor.
- Do not ask questions whose answers will not change the lesson.
- Do not force Socratic guessing before the learner has a usable representation.
- Do not create prolonged or unsafe failure.
- Do not use fake controls or decorative diagrams.
- Do not bury the direct answer behind pedagogy.
- Do not infer durable competence from confidence, fluency, or one correct guess.
- Do not claim that a reminder, file, image, app, or interaction exists unless it was actually created and verified.

## Supporting references

- `references/evidence.md`: research basis, limits, and source links
- `references/capability-modes.md`: format decisions, fallbacks, and accessibility
- `references/learner-model.md`: optional private adaptation schema and update rules
