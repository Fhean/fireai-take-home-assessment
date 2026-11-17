# FireAI Take-Home Assessment — Projects A & B

**Author:** Mohamed Farhanudin S  
**Assessment areas:** AI/ML Engineer and SDE1

This public repository consolidates the five materials submitted for the FireAI take-home assignment: the Project A results and architecture note, Project B results and pipeline note, decision matrix, AI usage note, and Python codebase.

## Repository contents

```text
.
├── README.md
├── REPRODUCIBILITY_AND_SCOPE.md
├── requirements.txt
├── docs/
│   ├── AI_USAGE.md
│   ├── DECISION_MATRIX.md
│   ├── PROJECT_A_RESULTS_AND_ARCHITECTURE.md
│   └── PROJECT_B_RESULTS_AND_PIPELINE.md
├── src/
│   └── fireai_assessment_codebase.py
├── tests/
│   └── test_smoke.py
└── archive/
    └── original-submission/
        └── fireai_assessment_codebase.py
```

## Project A — Income-tax engine

The results note compares deterministic hand-coded rules, query-time LLM execution, and LLM-compiled rule generation. It recommends deterministic calculation logic, with an LLM constrained to natural-language intent extraction and clarification. The note records the FY 2024–25 to FY 2025–26 rule-transition discussion and the reported comparison measurements. See [docs/PROJECT_A_RESULTS_AND_ARCHITECTURE.md](docs/PROJECT_A_RESULTS_AND_ARCHITECTURE.md).

## Project B — NYC 311 data-quality pipeline

The results note describes a layered data-quality approach using schema/rule checks, statistical profiling, and selective LLM review for semantic cases. It records the 12 corruption categories, reported detector measurements, and a 50-million-rows-per-day scale design. See [docs/PROJECT_B_RESULTS_AND_PIPELINE.md](docs/PROJECT_B_RESULTS_AND_PIPELINE.md).

## Decision rationale and AI use

- [docs/DECISION_MATRIX.md](docs/DECISION_MATRIX.md) maps components to deterministic, statistical, or hybrid approaches and records the stated measurement-based rationale.
- [docs/AI_USAGE.md](docs/AI_USAGE.md) records the AI tools and workflow described in the submission, including an example of an AI-generated formula that was caught and corrected during validation.

## Run the included Python sample

The included sample uses only the Python standard library. From the repository root:

```bash
python src/fireai_assessment_codebase.py
python -m unittest discover -s tests -v
```

The runnable file in `src/` corrects a syntax issue in the supplied script: an `@dataclass` decorator was placed immediately before a dictionary assignment. The submitted version is retained in `archive/original-submission/` for traceability; the author's email address has been omitted from public code copies.

## Reproducibility and limitations

Please read [REPRODUCIBILITY_AND_SCOPE.md](REPRODUCIBILITY_AND_SCOPE.md) before interpreting the reported results. The supplied Python file is a **consolidated demonstration subset**, not a complete implementation of every component described in the results notes. This snapshot does not contain the full 200+ tax test cases, the complete 12-type corruption injector/detector implementation, benchmark/load-test harnesses, or the underlying NYC 311 fixtures required to independently regenerate all reported metrics.

The documents preserve the measurements and design claims as recorded in the submitted results notes. They should not be interpreted as independently reproduced by this repository snapshot. The tax functions in the sample are simplified examples, not a production tax calculator or legal/tax advice. The added smoke tests check only the small sample included here; they do not validate statutory tax correctness or substantiate the full benchmark figures.

## Runtime

- Python 3.9 or later recommended
- No third-party packages required for the included sample
