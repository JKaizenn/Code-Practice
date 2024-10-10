# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. It is often used in algorithm examples, and is defined by the following formula: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.

# Your task is to implement the Fibonacci algorithm in three different methods: 1. Recursively 2. Iteratively 3. Using Memoization

# Example 1:

# Input:

# n = 5
# Output:

# fibonacci(n) -> 5
# Example 2:

# Input:

# n = 10
# Output:

# fibonacci(n) -> 55
# The Fibonacci sequence starts as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…




def main():
    print(recursive_fibonacci(5))
    print(iterative_fibonacci(10))
    print(memoization_fibonacci(10))
    
#Recursive Method 
def recursive_fibonacci(f):
    def fibonacci(n):
        if n <= 1: 
            return n 
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    return fibonacci(f)

#Iterative Method
def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

#Memoization Method
def memoization_fibonacci(n):
    memo = {0: 0, 1: 1}
    def fibonacci(n):
        if n not in memo:
            memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    return fibonacci(n)

# Time complexity: O(n)
if __name__ == "__main__":
    main()