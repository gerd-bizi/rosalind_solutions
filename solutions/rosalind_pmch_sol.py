import math

class Solution:
    def num_perfect_matchings(RNA):
        """
        Logic:
        First, we must consider how many perfect matchings there are between AU: 1
        AUAU (any order): 2
        AAAUUU: 6
        Factorial relation, trivial proof
        Now, we also have the GC's, which pair together.
        Multiply both numbers to get total number of perfect matchings
        """
        print(math.factorial(RNA.count('A')) * math.factorial(RNA.count('G')))
                        


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
        RNA = read_fasta("../problems/rosalind_pmch.txt")[0]
        num_perfect_matchings(RNA)