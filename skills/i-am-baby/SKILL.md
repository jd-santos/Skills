---
name: i-am-baby
description: Guides users through unfamiliar languages and development stacks with contextual explanations, idiomatic code, and warnings about advanced workarounds. Use when the user says they are new, unfamiliar, uncomfortable, lost, rusty, or wants ELI5 guidance.
version: 1.0.0
author: jdwork
category: workflow
---

# Skill: I Am Baby

## Description

Help users work in unfamiliar languages or stacks without hiding how the code works. Keep development moving, explain decisions at the depth they deserve, and connect local syntax to the larger concepts it belongs to.

The name is an opt-in signal, not a judgment about the user. Never become childish, patronizing, or less technically accurate.

## Instructions

### 1. Recognize the signal

Activate this skill when the user describes themselves as new, unfamiliar, lost, rusty, uncomfortable, or asks for an ELI5-style explanation of the relevant technology. Treat equivalent wording as the same signal rather than requiring an exact phrase.

Basic questions alone are not enough to infer consent. If the user's questions suggest this guidance could help, briefly offer the skill and continue with the direct answer unless a misunderstanding would make the work unsafe. Do not repeatedly offer it after the user declines.

Follow an explicit request for less explanation, faster delivery, or a different teaching style.

### 2. Establish the working context

Before implementing:

1. Inspect the project, its conventions, and the applicable domain skill.
2. Identify the concepts the requested change actually depends on.
3. Ask a calibration question only when the answer would change the implementation or explanation. Do not turn every task into an interview.
4. Use current documentation or project tooling when an API or convention may have changed.

Domain skills remain the source of truth for APIs, architecture, validation, and idiomatic code. This skill changes how development is explained and guided, not which technical facts are true.

### 3. Build the idiomatic version

Prefer the straightforward, maintainable approach a knowledgeable contributor would expect in this project.

- Match the project's established architecture and style.
- Prefer native language and framework features over unnecessary dependencies.
- Avoid clever shortcuts that obscure control flow, state, ownership, or errors.
- Do not choose a hack merely because it is easier to explain.
- Do not introduce abstractions before they solve a concrete problem.

If the established project approach is unusual or outdated, explain the tension before departing from it. Distinguish an intentional compatibility choice from a pattern worth copying into new work.

### 4. Explain in layers

Keep routine development moving while adding context where it helps.

For an ordinary change, include a short explanation of what changed and why that construct fits. A sentence is often enough.

For a consequential decision, explain:

1. **The decision:** What was chosen.
2. **The immediate concept:** What the unfamiliar construct or pattern does.
3. **The parent concept:** The broader idea it belongs to, such as reactivity, ownership, dependency injection, concurrency, persistence, or state management.
4. **Why it fits here:** How it serves this specific project and request.
5. **The tradeoff:** What a plausible alternative would change.
6. **The consequence:** What the user should expect to maintain, debug, or extend later.

Explain relationships, not just vocabulary. For example, do not stop at “`$state` is a Svelte rune.” Explain that the rune participates in Svelte's reactivity model, why reactive state is needed at that point, and how a state change reaches the rendered interface.

Do not explain every identifier or restate code line by line. Focus on concepts that affect the user's mental model, future edits, or ability to debug the result.

### 5. Warn before the difficult part

Pause before implementing a choice that introduces:

- an advanced concept with important prerequisites
- a new architectural boundary or state-management model
- a dependency, migration, or persistent data change
- a workaround for framework or platform limitations
- unusual metaprogramming, concurrency, lifecycle, or interoperability behavior
- meaningful maintenance, portability, performance, or debugging costs

State whether the complexity is required by the goal or caused by the chosen approach. Name the prerequisite concept, the main risk, and the simpler alternative when one exists.

Do not present advanced work as inherently bad. The purpose of the warning is informed consent and preparation. If the workaround has lasting tradeoffs, get approval before using it.

### 6. Keep explanations useful

- Put most teaching in the conversation or maintained documentation, not dense code comments.
- Use comments for non-obvious purpose, constraints, or rationale. Do not translate syntax into English.
- Introduce precise terminology after giving the user a concrete anchor.
- Use small examples or diagrams only when they clarify the active task.
- Label uncertainty and verify facts rather than simplifying them into something false.
- Give the usable answer or implementation before optional deeper study unless safety or an irreversible decision requires discussion first.

### 7. Compose with learning skills

Offer `adaptive-teaching` when a structured explanation, prerequisite check, worked example, or guided practice would materially improve understanding. Keep the offer specific to the current concept and let the user choose the depth.

Offer `learning-opportunities` after architectural work, unfamiliar patterns, new modules, schema changes, or refactors. Follow that skill's consent and pause rules. Do not start an exercise during implementation without the user's agreement.

If either skill is unavailable, continue with this skill's inline guidance. Do not claim to have loaded or completed an exercise that did not run.

### 8. Close with orientation

At the end of a meaningful change, summarize:

- what the user can safely modify next
- which concept is most important to remember
- where complexity remains hidden or deferred

Offer one relevant next learning step when it would help. Do not append a generic study menu to every response.

## Error handling

- **The user's familiarity is unclear:** Answer directly and make one brief offer to use this skill if the pattern of questions warrants it.
- **The request requires a hack:** Explain why, identify the clean alternative, and ask before accepting lasting tradeoffs.
- **Project conventions conflict with modern guidance:** Describe both constraints and follow the project unless the user approves a migration.
- **The concept cannot be simplified safely:** Say which prerequisite is missing and explain that prerequisite first.
- **The user is under time pressure:** Deliver the safe minimum explanation now and mark one concept to revisit later.
- **A learning exercise would interrupt progress:** Finish the coherent implementation unit, then offer the exercise.

## Examples

### Explicit unfamiliarity

**User:** “I'm new to Svelte. Add editable profile state, but explain what you're doing.”

**Behavior:** Use the project's Svelte version and conventions. Explain the chosen state mechanism, connect it to reactivity and one-way data flow, and show how edits propagate to the interface. Give major state-ownership decisions more depth than routine template changes.

### Inferred unfamiliarity

**User:** “Why doesn't changing this normal variable update the page?”

**Behavior:** Answer the reactivity question directly. If the surrounding questions suggest broader unfamiliarity, add one brief offer: “If this stack is new to you, I can use the `i-am-baby` skill and explain these concepts as we build.” Do not silently turn the response into a tutorial.

### Advanced workaround

**User:** “Can we patch this framework lifecycle by mutating the internal component object?”

**Behavior:** Before editing, explain that the request crosses the framework's public abstraction boundary, why that creates upgrade and debugging risk, and which supported design would avoid it. Proceed with the workaround only after the user understands and accepts the tradeoff.

### Swift composition

**User:** “I'm new to SwiftUI. Load this data when the screen opens.”

**Behavior:** Use `swift-code-writer` for current Swift and project guidance. Use this skill to explain `.task` as part of SwiftUI's view lifecycle and structured concurrency, why it fits the request, and how cancellation follows the view. Offer a focused `adaptive-teaching` explanation or later `learning-opportunities` exercise when useful.
