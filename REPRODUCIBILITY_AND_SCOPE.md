# Reproducibility and scope

This repository reflects the five assessment materials supplied for review and keeps a public-safe copy of the submitted consolidated Python file for traceability.

## Included

- Project A results and architecture note
- Project B results and pipeline note
- Decision matrix
- AI usage note
- Consolidated Python sample with selected Project A tax functions and selected Project B data-quality examples
- A syntax-corrected runnable copy of the sample
- Small smoke tests for the functions and checks present in that sample

## Not included in this repository snapshot

- The complete 200+ test-case suite referenced in the Project A results note
- A complete implementation of all 12 Project B corruption types and detectors
- The benchmark and load-test harnesses required to independently recreate all reported accuracy, latency, cost, false-alarm, and throughput figures
- The underlying data fixtures used for those measurements

Accordingly, the results documents preserve the findings and measurements as reported in the submitted materials; this repository does not independently reproduce all of them. The included Python sample is a limited demonstration subset. Its tax calculations are simplified and must not be treated as production-grade statutory calculations or tax advice.

The source copy under `archive/original-submission/` preserves the submitted script's code structure, with the author's email address omitted from the public copy. The runnable `src/` version fixes the decorator/syntax issue so the sample can execute. This syntax correction does not validate the tax logic.
