class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(n) for n in num]
        num = int("".join(num)) + k
        return map(int, str(num))
        