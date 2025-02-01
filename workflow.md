## Find the cancer SNPs
We begin with [a paper](https://pubmed.ncbi.nlm.nih.gov/31410488/) that did a GWAS on cancer patients. 

[This database](http://ibi.hzau.edu.cn/ncRNA-eQTL/cis.php) has SNPs that were found in people with cancer. 

## Find the sequences
We have to get a fasta file with the gene sequence for each SNP. 
https://www.ncbi.nlm.nih.gov/nuccore/NC_000004.12?report=fasta&from=84965616&to=85008743

### DNA to RNA
Just replace the T's with U's or
http://biomodel.uah.es/en/lab/cybertory/analysis/trans.htm

## Predict structure
Then we need to predict the secondary structure of the RNA. [This paper](https://arxiv.org/abs/2204.00300) predicts the structure. 

They made an online version for RNA secondary structure prediction: https://proj.cse.cuhk.edu.hk/rnafm/#/

Here's a kaggle page: https://www.kaggle.com/code/thetaiotaomacron/rna-fm/edit


Different RNA secondary structure predictors:
https://rna.urmc.rochester.edu/RNAstructureWeb



### Creating pretty pictures with AI:
![AI generated RNA mutation](https://github.com/user-attachments/assets/a8261c42-5729-4ee8-bfa5-17919d0b75bf)

https://huggingface.co/spaces/stabilityai/stable-diffusion \
https://designer.microsoft.com/image-creator?scenario=texttoimage \
https://copilot.microsoft.com/onboarding \
https://www.doubao.com/ 
