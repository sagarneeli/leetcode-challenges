class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i, ch in enumerate(s):
            if i % 2:
                count += 1 if ch != '1' else 0
            else:
                count += 1 if ch != '0' else 0
        return min(count, len(s) - count)

            
        