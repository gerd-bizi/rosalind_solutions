import math

class Solution:
    def shared_motif(seqs):
        #Find the shortest sequence
        shortest = math.inf
        nuc_seq = ''
        for seq in seqs:
            if len(seq) < shortest:
                shortest = len(seq)
                nuc_seq = seq
        i = 0
        j = shortest
        lcsm = ''
        lcsm_len = 0
        while j > 1:
            while i < j:
                subseq = nuc_seq[i:j]
                print(i, j)
                works = True
                for seq in seqs:
                    if subseq not in seq:
                        works = False
                        break
                if works:
                    if len(subseq) > lcsm_len:
                        lcsm = subseq
                        lcsm_len = len(subseq)
                i += 1
            j -= 1
            i = 0
        print(lcsm)

        
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
        sequences = read_fasta("../problems/rosalind_lcsm.txt")
        shared_motif(sequences)