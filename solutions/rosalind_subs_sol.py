class Solution:
    def combing_through_haystack(s, t):
        seqlen = len(s)
        sublen = len(t)
        i = 0
        cand = []
        while i < seqlen:
            if s[i] == t[0] and i + sublen < seqlen:
                works = True
                for a in range(i + 1, i + sublen):
                    if s[a] != t[a - i]:
                        works = False
                        break
                if works:
                    cand.append(i + 1)
            i += 1
        ans = ''
        for num in cand:
            ans += str(num) + " "
        print(ans[:-1])
    
    if "__main__" == __name__:
        combing_through_haystack("CATCAGAAGGGATCAGAACATCAGAAGACTCAAGGCTAATCAGAAGTCCAATCAGAACCCCTAATCAGAAGTGATCAGAAAATCAGAATCCATCAGAAATCAGAAAATCAGAAACATCAGAACATCCCATCAGAAAGATCAGAAGATCAATCAGAATGCATCAGAAGTGCAAGCATCAGAACATCAGAACATCAGAAATTGGACCAATCAGAAATCAGAAGATCAGAAATCAGAAATCAGAAAAATCAGAATATCAGAACATCAGAAAGCATCAGAACCGATCAGAAAAATCAGAAATCAGAATCATCAGAAAATCAGAAATCAGAATATCAGAAGATCAGAAGGAAATCAGAAATCAGAACATCAGAAATCAGAATAATCAGAAAATCAGAAATCAGAAAGTCAGCACATCAGAATGTTGCATCAGAATTATCAGAAGAATCAGAACATCAGAAATCAGAAATCAGAAGCCATCAGAATCGCAATGATCAGAAATATCAGAAATCAGAAATCAGAAGATCAGAATTAGATCAGAAATCAGAACATCAGAATCTCCGATCAGAAATCAGAAATCAGAACATCAGAAAATCAGAACATCAGAACCTGAAAGTAGATCAGAAATCAGAAAAAATCAGAAATCAGAACTACAATCAGAAATCAGAACCATTACCATCAGAAATCAGAAGGGATCAGAAGCCAATCAGAAATGGCTACAGCGAAATCAGAAAAATCAGAATCTTGGATCATCAGAAATCAGAAATCAGAAGTATCAGAACATCAGAAAATCAGAAATCAGAATGCTGTATCAGAAGACCACCTCTATCAGAAACATCAGAAAGAGGTTATCAGAACCTCTGCCCGAGCCATCAGAAA", "ATCAGAAAT")