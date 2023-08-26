class Solution:
    def reverse_complement(seq):
        com = ''
        for nuc in seq:
            if nuc == 'G':
                com += 'C'
            elif nuc == 'C':
                com += 'G'
            elif nuc == 'A':
                com += 'T'
            else:
                com += 'A'
        return com
    
    def res(seq, com):
        i = 0
        while i < len(seq):
            for x in range(4, 13):
                if i + x > len(seq):
                    break
                sec_locus = seq[i:i+x]
                com_locus = com[i:i+x]
                com_locus = com_locus[::-1]
                if sec_locus == com_locus:
                    print(str(i + 1) + ' ' + str(x))
            i += 1

        
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
        sequence = read_fasta("../problems/rosalind_revp.txt")[0]
        reverse_complement = reverse_complement(sequence)
        res(sequence, reverse_complement)