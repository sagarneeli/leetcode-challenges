class Solution:
    def fib(self, n: int) -> int:
        # Base case: n = 0 or 1
        if n <= 1:
            return n

        # recursive case
        return self.fib(n - 1) + self.fib(n - 2)
        