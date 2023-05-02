class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_negative_numbers = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count_negative_numbers += 1
        
        if count_negative_numbers % 2 == 0:
            return 1
        
        return -1
        