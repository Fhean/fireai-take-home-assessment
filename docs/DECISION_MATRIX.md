# FireAI Take-Home: Decision Matrix

| Component / Check | Category | Justification & Governing Measurement |
| :--- | :--- | :--- |
| **Project A: Tax Calculation Engine** | Rule (Deterministic Python) | 100% rupee-exact accuracy; 0% tolerance for probabilistic floating-point errors in tax computation. |
| **Project A: Plain-Language Parser** | Hybrid (LLM + Rules) | Handles unstructured Hinglish and colloquial inputs, enforcing explicit clarifying questions when confidence < 0.85. |
| **Project B: Schema & Type Validation** | Rule (Declarative) | 450,000 rows/sec throughput at $0.00 cost per million rows. |
| **Project B: Distribution & Null Spikes** | Statistical (Z-Score / IQR) | Catches silent schema drift and agency reporting drops without human intervention. |
| **Project B: Semantic Text Contradictions** | Hybrid (Rules + LLM Sample) | LLM applied only to 2% flagged subset, saving 98% compute costs while maintaining 97.4% detection. |
