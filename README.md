# RNA_mutations
Our solution addresses the challenge of predicting and personalizing cancer treatment by focusing on non-coding RNA (ncRNA) variants. Despite the critical role of ncRNA in gene regulation and cancer pathology, it remains underexplored compared to protein and coding RNA mutations. Advancing innovation in this area is crucial for enhancing precision medicine and improving patient outcomes.

We leverage deep learning to evaluate how mutations disrupt the structural integrity of ncRNA and assess their potential pathogenicity in cancer. Drawing an analogy to a "banana," we hypothesize that mutations in specific structural regions (e.g., surface or tips) may have a disproportionate impact on RNA function. Our approach utilizes the pre-trained RNA-FM model to encode ncRNA sequences into a high-dimensional feature space (L × 640), capturing sequential and evolutionary information. These features serve as inputs to a predictive model trained on COSMIC data, enabling the identification of mutations likely to be cancer pathogenic variants.

By providing a framework to interpret patient-specific ncRNA variations, this solution bridges a critical gap in understanding non-coding regions and their contribution to cancer. Ultimately, it has the potential to transform how personalized cancer treatments are developed and delivered.

