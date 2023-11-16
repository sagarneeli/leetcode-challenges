class Solution:
    def fib(self, n: int) -> int:
        def helper(n):
            # Base case: n = 0 or 1
            if n <= 1:
                return n

            # recursive case
            return helper(n - 1) + helper(n - 2)
        
        return helper(n)
        