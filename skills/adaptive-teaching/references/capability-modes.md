# Capability Modes

Use the least expensive representation that supports the learning operation. Start with the information structure, then choose the medium.

## Detection and overrides

1. Check explicit user instructions.
2. Inspect reliable host metadata, supported syntax, and available tools.
3. Select the closest named profile.
4. Add or remove individual capabilities when the host exposes a mixed set.
5. If support is uncertain, choose `markdown` or `text` and preserve the richer option as code, not executable content.

Never infer support merely because a format exists in the model's training data.

## Named profiles

### `text`

Available: plain text and monospaced code blocks.

Use:

- short paragraphs and compact lists
- numbered steps
- key-value comparisons instead of wide tables
- ASCII diagrams for small flows, hierarchies, and states
- linear equations with variables and units defined

ASCII rules:

- Keep diagrams narrow enough for a phone.
- Put the takeaway before or after the diagram.
- Use labels, not shape alone, to carry meaning.
- Prefer indented lists when wrapping would destroy alignment.

### `markdown`

Available: headings, emphasis, lists, links, code blocks, and usually tables.

Use Markdown as the portable default. Keep tables to about three to five narrow columns. Below each table, state the decision rule or trend in prose.

Do not assume support for Mermaid, rendered math, collapsible sections, or raw HTML.

### `mermaid`

Available: Markdown plus Mermaid rendering.

Use Mermaid for:

- causal or process flows
- state transitions
- hierarchies and dependencies
- sequence or architecture relationships

Do not use it for a simple list or as decoration. Keep nodes concise. Follow every essential diagram with a textual relationship summary or compact ASCII fallback. If rendering fails, continue the lesson with the fallback instead of debugging presentation syntax unless the diagram itself is the task.

### `rich`

Available: safe inline HTML/CSS, rendered math, or image generation. Capabilities may differ, so confirm each one.

Use HTML/CSS for semantic layout that Markdown cannot express clearly. Prefer native semantic elements. Avoid active scripts, remote dependencies, hidden essential content, and styling that breaks copy/paste or linear reading.

Generate an image only when spatial or perceptual form carries information that prose, data, or a diagram cannot communicate efficiently. Provide concise alt text and, for complex images, a purpose statement plus a detailed description or data equivalent.

### `interactive`

Available: MCP Apps, sandboxed HTML/JavaScript, notebooks, or equivalent stateful controls.

Interaction must change a learning-relevant variable, decision, representation, or feedback state. Good uses include:

- manipulating an input and predicting the result
- stepping through a state transition
- testing several cases with immediate explanatory feedback
- exploring a branching scenario with consequential outcomes
- building or rearranging a model that can be checked

Require a static fallback that teaches the same relationship through selected cases. Do not build an app when a one-line response or small table yields the same learning value.

Before creating active content, verify the sandbox and delivery surface. After creation, exercise the important controls and verify the resulting states. Do not claim the interaction works from source inspection alone.

## Selection matrix

| Learning structure | Default | Enhancement | Static fallback |
| --- | --- | --- | --- |
| Definition or rationale | Prose | Highlighted takeaway | Plain paragraph |
| Ordered procedure | Numbered steps and code | Runnable example | Copyable code plus expected result |
| Comparison | Narrow table | Sortable/filterable table | Repeated labeled bullets |
| Hierarchy or causal chain | ASCII or indented list | Mermaid | Numbered relationship summary |
| State transition | State table | Mermaid state diagram | `state + event -> state` lines |
| Quantitative relationship | Equation plus example | Rendered math or manipulable values | Linear equation and hand-worked values |
| Physical layout or visual pattern | Structured description | Generated image | ASCII sketch or coordinate description |
| Variable exploration | Selected static cases | Slider, notebook, or MCP App | Prediction table with answer key |
| Branching judgment | Scenario and decision points | Interactive branch | Static case tree |
| Dense data | Small table and takeaway | Accessible chart | Data table plus stated trend |

## Visual checks

Before adding a visual, answer:

1. What relationship becomes easier to see?
2. Is that relationship important to the stated outcome?
3. Is the visual faster to interpret than good prose or a table?
4. What is the text equivalent?
5. Will it still work on the learner's device and access path?

If the first three answers are weak, omit it.

## Accessibility and degradation

- Essential meaning must survive without CSS, JavaScript, Mermaid, images, audio, hover, or animation.
- Never use color, position, shape, or motion as the only signal.
- Give controls accessible names, roles, states, values, errors, and status updates.
- Ensure keyboard operation, visible focus, readable order, zoom, high contrast, and reduced motion.
- Label axes, units, series, and the takeaway for charts. Provide values or a detailed text alternative.
- Caption or transcribe audio and video.
- Avoid autoplay, forced scrolling, timed expiration, flashing, and focus traps.
- Test mobile wrapping and copy/paste for any representation the learner may reuse.

## Fallback ladder

```text
interactive -> selected static cases
image       -> structured description or ASCII
Mermaid     -> ASCII or numbered relationships
HTML        -> semantic Markdown
wide table  -> repeated labeled bullets
rendered math -> linear text equation
```

Fallbacks preserve the concept, not the appearance.
