class Solution:
    def reading_and_writing(filename):
        f = open(filename, "r")
        lst = f.readlines()[1::2]
        f_prime = open("rosalind_ini5_out.txt", 'w')
        for l in lst:
            f_prime.write(l)
        f.close()
        f_prime.close()
    
    if "__main__" == __name__:
        reading_and_writing("../problems/rosalind_ini5.txt")