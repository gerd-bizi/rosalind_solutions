class Solution:
    def condiitons_and_loops(a, b):
        summ = 0
        while a <= b:
            if a % 2 == 1:
                summ += a
            a += 1
        print(summ)


    if __name__ == "__main__":
        condiitons_and_loops(4779, 9765)