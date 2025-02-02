# RNA_mutations
### Unlocking the Power of ncRNA--Classifying Pathogenic SNPs for Next-Generation Treatments

Our solution addresses the challenge of predicting and personalizing cancer treatment by focusing on non-coding RNA (ncRNA) variants. Despite the critical role of ncRNA in gene regulation and cancer pathology, it remains underexplored compared to protein and coding RNA mutations. Advancing innovation in this area is crucial for enhancing precision medicine and improving patient outcomes, particularly in breast cancer. 

We leveraged deep learning to evaluate how mutations disrupt the structural integrity of ncRNA and assess their potential pathogenicity in cancer. Drawing an analogy to a “banana,” we hypothesized that mutations in specific structural regions—such as the surface or tips of the RNA may have a disproportionate impact on RNA function, just as a small change at the tip of a banana may cause a larger structural shift. Our approach utilized the pre-trained RNA-FM model to encode ncRNA sequences into a high-dimensional feature space, capturing both sequential and evolutionary information. These features serve as inputs to a predictive model trained on SNPs associated with cancer survival (ncRNA-eQTL) and neural SNPs (dbSNP) databases. 

Overall, our approach identifies druggable regions within ncRNA, pinpointing structural vulnerabilities that could serve as novel therapeutic targets. In breast cancer certain SNPs in ncRNA have been identified that disrupt the secondary structure of the RNA, impairing tumor suppressor genes. These mutations may contribute to tumor progression, highlighting the potential importance of ncRNA variants in cancer treatment. This has the potential to transform personalized oncology treatment by identifying key biomarkers and guiding targeted therapeutic strategies across multiple disease types.

![3abf4388-af4e-4c99-8107-7921c24f3bb5](https://github.com/user-attachments/assets/aa708a5b-f2ee-4d14-a6b1-d07a8b580658)
