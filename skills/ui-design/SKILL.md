---
name: ui-design
description: Designs clear, restrained, accessible application interfaces and reviews UI hierarchy, controls, responsive behavior, and states. Use when designing, implementing, or critiquing UI/UX, frontend screens, forms, dashboards, or component layouts.
version: 1.0.0
author: jdwork
category: workflow
---

# Skill: UI Design

## Description

Design application interfaces that are clear, efficient, restrained, accessible, and visually intentional.

The goal is not minimalism. The goal is **high information clarity with low visual overhead**. Avoid the generic AI-generated look of excessive cards, large rounded containers, pills, decorative gradients, oversized spacing, and too much explanatory copy.

## Instructions

### Core principles

#### Design around the task

Identify the user’s primary task first. Make that action easy to find and perform before presenting secondary dashboards, explanations, configuration, or historical information.

Do not give every available piece of information equal prominence.

#### Structure before styling

Establish the information architecture using:

- hierarchy
- typography
- spacing
- alignment
- reading order

before introducing cards, borders, backgrounds, or decorative treatments.

A logical component does not need to be a visually boxed component.

#### Use the least visual structure necessary

Prefer, in order:

1. proximity
2. alignment
3. typography
4. whitespace
5. dividers
6. subtle surface changes
7. borders
8. cards or strong containers

Do not put something in a box unless the boundary communicates useful meaning.

#### Avoid card proliferation

Do not turn every metric, setting, paragraph, or subsection into a card.

Prefer rows, lists, tables, definition grids, columns, or simple sections when they communicate the same information more efficiently.

Cards are appropriate when something is meaningfully independent, interactive, selectable, movable, or needs strong separation.

#### Keep geometry restrained

Use a small radius scale. Avoid large rounded corners everywhere.

Reserve fully rounded pills for actual:

- tags
- filters
- statuses
- tokens
- segmented controls

Do not turn descriptive phrases or ordinary buttons into pills by default.

#### Keep visible copy concise

Interfaces are not documentation.

Prefer a short title, an optional one-line explanation, and the relevant action. Avoid repeatedly stacking:

- eyebrow
- heading
- subtitle
- paragraph
- badges
- alert
- action

Use progressive disclosure for secondary explanations, advanced options, edge cases, and technical details.

Important safety or consequence-related information may remain prominent.

#### Favor information density over component density

Dense does not mean cramped.

Related information should be close together and easy to scan without requiring a separate padded container for every value.

Use generous spacing **between groups** and efficient spacing **within groups**.

#### Create hierarchy through emphasis

A typical task-oriented viewport should have:

- one dominant task or clear focal element
- a few secondary elements
- mostly quiet supporting information

If everything uses accent colors, badges, filled surfaces, and bold typography, nothing is emphasized.

#### Give color specific jobs

Use color semantically and sparingly.

Define roles such as:

- primary/action
- neutral
- success
- warning
- error
- information

Do not use brand color merely to make every section visually interesting.

Never rely on color alone to communicate status.

### Controls and data

Prefer conventional controls over novel UI patterns.

Use:

- checkboxes for independent options
- radios for mutually exclusive choices
- segmented controls for a few closely related modes
- tables for structured comparison
- lists for list-shaped information
- buttons with clear action labels

Do not replace familiar controls with selectable cards unless the card presentation adds real value.

Do not avoid tables just because cards look more modern.

### Forms

Forms should prioritize:

- visible labels
- logical ordering
- concise contextual help
- sensible defaults
- clear validation
- predictable keyboard navigation

Do not use placeholder text as the only label.

Put instructions next to the field they explain rather than in large introductory paragraphs.

### States

Design important states and interaction feedback intentionally:

- loading
- empty
- partial data
- unknown
- error
- offline
- disabled
- read-only
- success
- hover, pressed, focus, pending, and completion feedback

Do not treat **unknown**, **zero**, **none**, **loading**, and **error** as equivalent.

Loading states should preserve the eventual layout where practical and avoid unnecessary layout shifts.

### Responsive design

Responsive design is not merely converting columns into a vertical stack.

Reconsider hierarchy for smaller screens. Secondary information may move, collapse, or disappear while primary actions become easier to reach.

Likewise, desktop layouts should use available width effectively rather than looking like stretched mobile screens.

### Accessibility

Accessibility is part of the initial design, not a cleanup pass.

Maintain:

- sufficient contrast
- visible keyboard focus
- semantic controls
- associated form labels
- sensible heading structure
- usable interaction targets
- non-color status indicators
- screen-reader-friendly state changes
- accessible validation
- reduced-motion support
- functional zoom and text scaling

Do not make important text faint in pursuit of a cleaner appearance.

### Default aesthetic

When an existing design system, platform convention, or explicit product direction exists, follow it unless it conflicts with accessibility, usability, or the primary task. When none exists, prefer:

- restrained contemporary application UI
- crisp typography
- strong alignment
- moderate information density
- mostly neutral surfaces
- limited border radius
- minimal shadow
- subtle dividers
- sparing accent color
- compact but accessible controls

The result should feel like software designed for repeated daily use, not a startup landing page or component-library demo.

Avoid automatically adding:

- giant rounded cards
- pill-shaped everything
- glassmorphism
- glowing gradients
- decorative blobs
- icon bubbles on every item
- meaningless charts
- uppercase eyebrow labels on every section
- marketing-style hero copy inside application workflows

### Design process

Before implementation, inspect existing design tokens, components, platform conventions, and product language. Extend those conventions unless they conflict with accessibility or task clarity.

1. Identify the primary task and required supporting information.
2. Sketch the screen as an **unstyled text hierarchy**.
3. Establish layout and reading order.
4. Add familiar controls.
5. Add only the visual structure necessary to clarify hierarchy.
6. Design loading, error, empty, and responsive states.
7. Verify accessibility.

Do not let a component library determine the information architecture.

### Final review

Before finishing, perform four quick passes.

**Subtraction:** Remove borders, backgrounds, badges, icons, copy, and containers that do not add meaning.

**Hierarchy:** Confirm the primary task is immediately obvious and secondary information is appropriately quiet.

**AI-pattern check:** Look specifically for excessive cards, pills, large radii, repeated section intros, decorative color, and unnecessary explanatory text.

**Accessibility:** Verify that simplification did not remove labels, focus states, contrast, affordances, or semantic meaning.

### Guiding rule

> Prefer typography, alignment, whitespace, and familiar interaction patterns over decorative containers. Add visual structure only when it communicates something.
