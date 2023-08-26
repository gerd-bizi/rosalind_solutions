class Solution:
    def reading_and_writing(filename):
        dic = {}
        curr = ''
        with open(filename, 'r') as reader:
            for line in reader.readlines():
                line = line[:-1]
                if line[0] == '>':
                    dic[line[1:]] = ''
                    curr = line[1:]
                else:
                    dic[curr] += line
        max_name = ''
        max_gc = 0
        for k in dic.keys():
            gc_content = (dic[k].count('G') + dic[k].count('C')) / len(dic[k])
            if gc_content > max_gc:
                max_name = k
                max_gc = gc_content
        print(max_name)
        print(max_gc*100)
    
    if "__main__" == __name__:
        reading_and_writing("../problems/rosalind_gc.txt")