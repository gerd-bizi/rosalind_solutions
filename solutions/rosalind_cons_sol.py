class Solution:
    def consensus_and_profile(filename):
        #read in the fasta separated by a line of format >Rosalind_x file and store the sequences in a numpy array
        lin = ''
        seqs = []
        with open(filename, 'r') as reader:
            for line in reader.readlines():
                if line[0] == '>':
                    seqs.append(lin)
                    lin = ''
                else:
                    if line[-1] == '\n':
                        line = line[:-1]
                    lin += line
        seqs.append(lin)
        seqs.pop(0)
        profile_matrix = [[0] * len(seqs[0]), [0] * len(seqs[0]), [0] * len(seqs[0]), [0] * len(seqs[0])] #a c g t
        for seq in seqs:
            i = 0
            for c in seq:
                if c == 'A':
                    profile_matrix[0][i] += 1
                elif c == 'C':
                    profile_matrix[1][i] += 1
                elif c == 'G':
                    profile_matrix[2][i] += 1
                else:
                    profile_matrix[3][i] += 1
                i += 1
        consensus = ''
        for i in range(len(seqs[0])):
            vals = [profile_matrix[0][i], profile_matrix[1][i], profile_matrix[2][i], profile_matrix[3][i]]
            index = vals.index(max(vals))
            if index == 0:
                consensus += 'A'
            elif index == 1:
                consensus += 'C'
            elif index == 2:
                consensus += 'G'
            elif index == 3:
                consensus += 'T'
        print(consensus)

        def print_profile_matrix(base, lst):
            to_print = base + ": "
            for val in lst:
                to_print += str(val) + " "
            to_print = to_print[:-1]
            print(to_print)

        print_profile_matrix('A', profile_matrix[0])
        print_profile_matrix('C', profile_matrix[1])
        print_profile_matrix('G', profile_matrix[2])
        print_profile_matrix('T', profile_matrix[3])

        
    if __name__ == "__main__":
        consensus_and_profile("../problems/rosalind_cons.txt")
            
        