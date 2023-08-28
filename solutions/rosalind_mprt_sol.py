import requests
import re

motif = re.compile('N[^P][ST][^P]')

class Solution:
    def N_glycosylation_motif_checker(proteins):
        for k in proteins.keys():
            sequence = proteins[k]
            loci = motif.finditer(sequence)
            if any(loci):
                print(k)
                loci_string = ''
                for locus in loci:
                    loci_string += str(locus.start() + 1) + " "
                print(loci_string)
        
    def read_proteins(file_path):
        proteins = {}
        
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                urlline = line.split('_')[0]
                fasta_url = 'https://rest.uniprot.org/uniprotkb/{}.fasta'.format(urlline)
                response = requests.get(fasta_url)
                fasta_data = response.text
                header, sequence = fasta_data.strip().split('\n', 1)
                sequence = sequence.replace('\n', '')
                proteins[line] = sequence
        
        return proteins


        
    if __name__ == "__main__":
        proteins = read_proteins("../problems/rosalind_mprt.txt")
        N_glycosylation_motif_checker(proteins)