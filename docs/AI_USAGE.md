# AI Usage Note (AI_USAGE.md)

* **Tools Used:** Gemini 1.5 Pro, GitHub Copilot, and Cursor IDE for rapid boilerplate generation, unit test scaffolding, and regex pattern tuning.
* **Workflow:** AI agents were utilized to draft initial test cases for Indian income tax slabs and generate synthetic corruption injection scripts for NYC 311 datasets.
* **Hallucination & Correction Example:** During the initial drafting of Project A's marginal relief formula for surcharge under Section 112A/111A and regular slabs, the LLM initially suggested a simplified linear approximation that violated rupee-exact precision at the ₹50L surcharge threshold.
* **How It Was Caught:** Caught during Task 1 test suite validation against the Income Tax Department's official calculator reference values. The formula was manually corrected to enforce exact statutory marginal relief calculation rules in Python.
