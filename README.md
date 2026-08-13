# SF Blog Agent

Merged writing system for the Forge blog. Replaces two Claude Projects.

- `rules/writing.md` sets voice, structure, truth rules, SEO, and LLM visibility. Every rule is tagged `[LINT]`, `[JUDGE]`, or `[HUMAN]`.
- `rules/positioning.md` holds product facts, pricing with source URLs and verification dates, and per-article-type playbooks.
- `rules/process.md` is the 9-step production process, research through publish.
- `assets/comparison-table.html` is the comparison table template used in almost every article.
- `lint/` will hold the deterministic checks for every `[LINT]` rule. Not built yet.

Byline: Frank Sondors, always.

All three rules files pass their own banned-word and punctuation rules.
