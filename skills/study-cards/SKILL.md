---
name: study-cards
description: Creates focused Markdown study cards from PDFs, images, web pages, notes, transcripts, documentation, and question banks, with provenance and Mochi-compatible syntax. Use when turning source material into flashcards, practice questions, exam-prep cards, or an importable Mochi deck.
metadata:
  version: "1.0.0"
  category: workflow
---

# Skill: Study Cards

Turn source material into a small set of strong retrieval prompts. The output is portable Markdown that Mochi can import. Mochi owns review and spaced repetition; this skill owns source judgment, card design, provenance, and export.

Honor user constraints such as exam scope, chapters, preferred card types, target depth, and topic emphasis. Ask only when a missing choice would materially change the result.

## Understand the sources

Inspect the material before drafting cards.

- For PDFs and slides, identify sections and page or slide numbers. Visually inspect diagrams and tables when extraction could miss their meaning.
- Treat screenshots and images as visual evidence. Interpret diagrams, UI state, highlighted regions, CLI output, and error messages instead of relying only on OCR.
- For web pages, retain the title, section heading, and URL. Prefer official documentation when verifying vendor-specific claims.
- In notes, transcripts, and conversations, distinguish fact from opinion, speculation, and unresolved questions.
- Keep question banks identifiable. Record the exam, bank title, publisher or provider, question identifier, and version or access date when available.

Do not silently promote a source's claim beyond its evidence. If an important technical claim is doubtful and research is available, verify it against an authoritative source. Attribute any added evidence separately.

## Choose what deserves a card

Do not convert the source paragraph by paragraph. Favor knowledge that benefits from retrieval:

- distinctions between easily confused concepts
- architecture choices and tradeoffs
- constraints, guarantees, limits, and meaningful defaults
- security or responsibility boundaries
- service relationships and configuration implications
- failure modes, diagnostic signals, and likely fixes
- terminology or exact values that genuinely require memory

Skip material that is obvious from context, better looked up than memorized, unsupported, duplicated, or included only to increase card count. Prefer one comparison or scenario that preserves a relationship over several fragments that lose it.

Choose the prompt form that fits the idea:

- **Recall:** retrieve one fact or relationship.
- **Contrast:** distinguish concepts that learners confuse.
- **Constraint:** recall a rule, limit, or guarantee.
- **Scenario:** choose and justify an option in a realistic situation.
- **Diagnosis:** infer a cause or missing configuration from symptoms.
- **Cloze:** hide an exact term or value with `{{answer}}`; use sparingly.

## Distinguish card roles

Every card has one role. This distinction is independent of prompt form.

- `#card/understanding`: an agent-authored concept, contrast, constraint, scenario, or diagnosis card.
- `#card/sample-question`: a question retained from an identified source bank. Preserve the supplied stem and choices when the user wants authentic practice. Keep the source's answer and rationale faithful.
- `#card/derived-practice`: a new or materially rewritten question based on a source question or concept. Never label a rewritten variant as a sample question.

For a sample question, add identity tags when the source supplies enough information:

```text
#exam/<provider>/<exam-id>
#question-bank/<provider>/<bank-slug>
```

Omit the exam tag if the exam is unknown, and omit the bank tag if the bank or provider cannot be identified. Keep the best available identity in the source footer instead of inventing a provider or exam. Use lowercase stable slugs, for example `#exam/aws/saa-c03`. Add `#source-tier/official`, `#source-tier/highly-rated`, or another user-defined tier only when the source or user supports that classification. Do not infer quality from branding alone. These independent tags let Mochi views select a known exam, bank, or source tier.

Topic and prompt-form tags are optional. Keep them lightweight, such as `#domain/networking`, `#service/elb`, or `#prompt/scenario`.

## Write the cards

Each card should:

- test one main idea with an unambiguous prompt
- include enough context to stand alone months later
- lead with a concise answer, followed by a short explanation only when useful
- preserve qualifications that affect correctness
- avoid giving away the answer on the front
- avoid overlapping another card unless the retrieval path is meaningfully different
- contain no facts unsupported by the cited source or separately attributed verification

For sourced sample questions, put the full question and choices on the front. Put the keyed answer and supplied rationale on the back. If the bank gives only an answer key, do not invent a rationale. If external verification reveals a likely error, preserve the original answer, flag the discrepancy, and cite the verifying source.

## Emit Mochi-compatible Markdown

Default to an import bundle with one `.md` file per card. Mochi treats each file in a Markdown folder import as a card. Do not put a README or other non-card Markdown inside an import directory.

Use a line containing `---` to separate front and back:

```markdown
A workload requires static IP addresses and TCP pass-through. Which AWS load balancer fits?

---

Network Load Balancer (NLB).

### Why

NLB operates at Layer 4 and supports static IP behavior. ALB provides HTTP-aware Layer 7 routing.

### Source

AWS Elastic Load Balancing documentation, “Network Load Balancers”: <source URL>

#card/understanding #exam/aws/saa-c03 #domain/networking #prompt/scenario
```

A sourced question uses the same structure but retains the original stem and choices, then identifies its bank:

```markdown
<question stem and answer choices>

---

**Answer:** <source answer>

### Rationale

<source rationale, if provided>

### Source

<bank title>, <question ID or location>, <version or access date>

#card/sample-question #exam/aws/saa-c03 #question-bank/provider/bank-name
```

Use descriptive filenames based on the tested idea or bank question ID. Organize folders by intended deck, exam, or domain when that helps the user, but do not claim that nested filesystem folders automatically create Mochi subdecks. Include referenced attachments with standard Markdown links and deliver the files alongside the cards.

## Review the bundle

Before delivery:

1. Remove weak and duplicate cards.
2. Verify each answer and qualification against its cited source.
3. Confirm that sample, derived-practice, and understanding roles are labeled correctly.
4. Check exam and question-bank tags for consistent slugs.
5. Check every card's `---` separator, attachment path, filename, and source footer.
6. Report the card count, folder layout, source coverage, and any unresolved ambiguity.

Do not summarize the whole source, build a scheduler, create a database, or implement a review application unless separately requested.

## Direct Mochi insertion

Markdown bundles are the default and remain the portable source of truth. When the user explicitly asks to insert cards through the Mochi API, read [references/mochi-api.md](references/mochi-api.md) before making requests.
