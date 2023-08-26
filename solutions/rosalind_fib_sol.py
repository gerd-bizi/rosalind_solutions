class Solution:
    def fib(n, k):
        #n is the number of months after 1st
        #k is the number of offspring for mature bunnies
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        i = 2
        lst = [1, 1]
        while i <= n - 1:
            next = k * lst[i - 2] + lst[i - 1]
            lst.append(next)
            i += 1
        print(lst[-1])
    
    if "__main__" == __name__:
        fib(36, 4)
    