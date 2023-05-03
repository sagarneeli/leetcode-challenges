class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer.append((set(nums1) ^ set(nums2)) & set(nums1))
        answer.append((set(nums1) ^ set(nums2)) & set(nums2))
        return answer
        