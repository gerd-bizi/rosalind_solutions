class Solution:
    def mendels_first_law(homo_dom, hetero, homo_rec):
        total = homo_dom + hetero + homo_rec
        homo_dom_homo_dom = homo_dom / total * (homo_dom - 1) / (total - 1)
        homo_dom_hetero = homo_dom / total * hetero / (total - 1) * 2
        hetero_hetero = hetero / total * (hetero - 1) / (total - 1)
        hetero_homo_rec = hetero / total * homo_rec / (total - 1) * 2
        homo_dom_homo_rec = homo_dom / total * homo_rec / (total - 1) * 2

        homo_dom_homo_dom *= 1
        homo_dom_hetero *= 1
        hetero_hetero *= 0.75
        hetero_homo_rec *= 0.5
        homo_dom_homo_rec *= 1

        prob = homo_dom_homo_dom + homo_dom_hetero + hetero_hetero + hetero_homo_rec + homo_dom_homo_rec

        print(prob)
    
    if "__main__" == __name__:
        mendels_first_law(27, 21, 16)