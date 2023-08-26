class Solution:
    def fibd(n, death: int):
        #n is the number of months after 1st
        #death is after however many months they die
        
        fib = [1, 1]
        count = 2
        while count < n:
            if count < death:
                fib.append(fib[-1] + fib[-2])
            elif count == death:
                fib.append(fib[-1] + fib[-2] - 1)
            else:
                fib.append(fib[-1] + fib[-2] - fib[-death - 1])
            count += 1
        print(fib[-1])

    if __name__ == '__main__':
        fibd(95, 20)