RNA_CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
    
DNA_TO_RNA = {
    'A': 'A',
    'C': 'C',
    'T': 'U',
    'G': 'G'
}

class Solution:
    def intron_removal(seqs):
        main_seq = seqs[0]
        for seq in seqs[1:]:
            main_seq = main_seq.replace(seq, '')
        return main_seq
    
    def transcription(seq):
        rna_seq = ''
        for nuc in seq:
            rna_seq += DNA_TO_RNA[nuc]
        return rna_seq
    
    def translation(seq):
        codon_len = len(seq) // 3
        amino_acid_seq = ''
        for i in range(codon_len):
            codon = seq[3 * i] + seq[3 * i + 1] + seq[3 * i + 2]
            amino_acid = RNA_CODON_TABLE[codon]
            amino_acid_seq += amino_acid
        return amino_acid_seq

        
    def read_fasta(file_path):
        sequences = []
        current_sequence = None
        
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith(">"):
                    if current_sequence is not None:
                        sequences.append(current_sequence)
                    current_sequence = ""
                else:
                    current_sequence += line
        
            if current_sequence is not None:
                sequences.append(current_sequence)
        
        return sequences


        
    if __name__ == "__main__":
        sequences = read_fasta("../problems/rosalind_splc.txt")
        mature_dna = intron_removal(sequences)
        mRNA = transcription(mature_dna)
        protein_string = translation(mRNA)
        print(protein_string)