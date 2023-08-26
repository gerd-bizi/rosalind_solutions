class Node:
    def __init__(self, fasta, seq):
        self.fasta = fasta
        self.seq = seq

    def get_fasta(self):
        return self.fasta
    
    def get_seq(self):
        return self.seq

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = dict()

    def add_node(self, fasta, seq):
        self.nodes.append(Node(fasta, seq))
        self.edges[fasta] = []

    def add_edge(self, node1_fasta, node2_fasta):
        self.edges[node1_fasta].append(node2_fasta) #directed
    
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges


class Solution:
    def overlap_graphs(filename):
        #read in the fasta separated by a line of format >Rosalind_x file and store the sequences in a numpy array
        lin = ''
        fastas = []
        seqs = []
        with open(filename, 'r') as reader:
            for line in reader.readlines():
                if line[0] == '>':
                    fastas.append(line[1:-1])
                    seqs.append(lin)
                    lin = ''
                else:
                    if line[-1] == '\n':
                        line = line[:-1]
                    lin += line
        seqs.append(lin)
        seqs.pop(0)
        g = Graph()

        for (fasta, seq) in zip(fastas, seqs):
            g.add_node(fasta, seq)
        
        nodes: list[Node] = g.get_nodes()

        for suf_seq in nodes:
            for pre_seq in nodes:
                if pre_seq.get_fasta() != suf_seq.get_fasta():
                    if suf_seq.get_seq()[-3:] == pre_seq.get_seq()[:3]:
                        g.add_edge(suf_seq.get_fasta(), pre_seq.get_fasta())
        
        edges = g.get_edges()
        edge_list = edges.keys()

        for node1 in edge_list:
            if edges[node1]:
                for node2 in edges[node1]:
                    print("{} {}".format(node1, node2))

        
    if __name__ == "__main__":
        overlap_graphs("../problems/rosalind_grph.txt")
            
        