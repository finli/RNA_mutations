import fm
import torch
from Bio import SeqIO

if __name__ == "__main__":
    model, alphabet = fm.downstream.build_rnafm_resnet(type="ss")
    batch_converter = alphabet.get_batch_converter()
    model.eval()  

    fasta_file = "/path../rna_sequences.fasta"  
    data = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_id = record.id
        sequence = str(record.seq)
        data.append((seq_id, sequence)) 
    print("Loaded sequences:\n", data[:10])

    batch_labels, batch_strs, batch_tokens = batch_converter(data)

    input = {
        "description": batch_labels,
        "token": batch_tokens
    }

    # Secondary Structure Prediction (on CPU)
    with torch.no_grad():
        results = model(input)
    ss_prob_map = results["r-ss"]
    print(ss_prob_map)
    print(ss_prob_map.shape)

    print("Available keys in results:", results.keys())
    
    print(results["logits"].shape) 
