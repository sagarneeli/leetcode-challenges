class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        
        if product > 1:
            return 1
        elif product < 0:
            return -1
        
        return 0
        