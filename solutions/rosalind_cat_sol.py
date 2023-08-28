import math

def perfect_matchings(rna):
    return math.factorial(rna.count('A')) * math.factorial(rna.count('G'))

def catalan_matchings(rna):
    """
    Algo:
    Partition sring into two (where each partition has even number of nucleotides)
    Call the method used in PMCH on both halves, multiply those together
    Iterate until done the whole string
    """
    total = 1
    for i in range(1, len(rna) // 2 + 1):
        front = rna[:2 * i]
        back = rna[2 * i:]
        iteration_total = 1
        if len(front) > 2:
            iteration_total *= catalan_matchings(front)
        else:
            iteration_total *= perfect_matchings(front)
        if len(back) > 2:
            iteration_total *= catalan_matchings(back)
        else:
            iteration_total *= perfect_matchings(back)
        total += iteration_total
    return total
                    


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
    RNA = read_fasta("../problems/rosalind_cat.txt")[0]
    print(catalan_matchings(RNA))