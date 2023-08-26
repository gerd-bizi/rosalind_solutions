class Solution:
    def counting_point_mutations(u, v):
        count = 0
        for i in range(len(u)):
            if u[i] != v[i]:
                count += 1
        print(count)
    
    if "__main__" == __name__:
        counting_point_mutations(
            "TGTACAATCTCTAAGTCTGTCGCTAGCCCAACCACCTCGTATTAAGGTGCGGTCCAGAAAATGTATTCTGTCCACAGTTTCATTTCCAGTAGTAAGAGTGGCCGGAAAATATTAAAATATATTGCATGTGTCGTTAAGCCGGTTCAATCATAGAGTTATCGTTCTGAAAAGCCATCTCGCGGCTCGTCAATCCGGTATAGTGGCCAACCTAGGCAATTCCGGAAGGTGAAACGTCGTTGGAGACAATTCAGCGCGAGGATCACGGTGCTATACCCACTACAAGGTCGCTACGAGTCAGGAGCGGAGATTCAAGGACTTGTGGCGTCTCCCAGCAAGCCTAACCCCTCCAATGCTGCAGCACCTTATGGCTAGTCACGGTCGTAAGTCCGGTAACCTGAGTAAAATGGTCTCTTTAAATACTATGACGGCCGCACTGCAGCACACCCAGTTGACATTAACGAGGTTTAAAGGCTCGTAGTTGTTCCCCTGAAGGCCTCGAGTAAAATAAAACCACACTATTCATATCACGGGACCTCGGAGCTCCTCACTTTCCGAGGTGTACTTCAAATACCCCAAGCGTGCTCGAGTCAAAACTGAGGCAGTGGAAGTGCGAGCGCAAGTGGCATCAATCGATAAACTAGATCAGTGATTGTTGTGGCGTCAACGACAAGATGGCTGGACAAACATTCGTCGACAGACCGCTTAGGCTCTACCTGAGAAATATAGGTCTGTATTCGGGCTCCACATGGTGCAGGAATAGAAAATACGATATGACTCGCTACAGACCGCTTGTTGGTCTCGCTAGACTGTAGATTAGGGCCGCATCCGTGCCCGTCGTGGACTCCACCAGGATGTGTAGTATCTCGGAGCACTGTATAACTGCCGTAGGGTCGAGCCGTCACTCTAACTATTCAGCCAGTGGATCTAATGGGCGCAGGACCCCGTACCATTTGTGCCCGATGCCTGCTAGATGTGGAG",
            "GTAACCTTCTGAACGTGTCAATCTAGCCCACCCACGTCGTGTCAGCGTGTGACCTAGCAAAACGAAGCCGTCTACCACGTCAACACCGAGTGATGTAGTTGTTGGTCAACGATCATACGTATTCATAGCTTCATTTGGACAGTGCACTTATCGACCCATAGGTGTAACGAGGCACAGCGGGTTACTCGCCTAGGGTCTACCGTCTACCACGTGCAAGATCCGAATTATTTGCGTCTCTGGCCTACGAATGGTGCGAGGAAGAGGGAGCCATAGCGAACATAGTGTAGCTTCGTGGGAAGTGCGGTGATGGGTTGCAGAAACGTGTGCGTCTGGAAACGGAGCCCGTGGGATGGTTACCGAATCTGAAGGTAGTGAGGATGGAACTTGCTGGACAGTTAGGCAGGAGCCCTCCTTGAATGGTGACACGAACATCCTGAAGTAACACCTACGGATGTTACCGGCTATAGAAGGCACCCTGGTGCAGCCATCATGAGACCCGCGCGTAGAACACCTGGCTGTAAAGTTGACGGATGGTGCAGACGAGTGCCTTCCCTTCTGGGTGGACATAACCAGTTTGGCGGGCGGAGGCATCGCAGAGGCCGGGAACGTGCGACCGCGAAGGTAAGAACGTCCTAAACTCGATGCGTGACTGTTGACGCGACATCGCGATTCCTGTAGGAGAAATTTGCTTCAATAGAACGATTAAAGTACGCCAGAGAAATAGACGCTGGCAGTTACCTACGGAAGGTGCTCGGTAGAGATAAAACCATATGACGCTCAAACGAGCGCCAGATAGTCGAGATCCTATGAAGATGTGTCCCAAATCCTCGAATGGCCCCGATGCCTCCGTCACGAGTAGCTTTTATTCGCGCCGTAGACCTGCGGGAGGAGTAAAGCTTTACTGCGACTATTCGGAGTCTAGATAGAAGGGAGCCGCGAATCGGTACCGTTTGTGGCCGGTGCCAGTTCGTTGTGATG"
        )