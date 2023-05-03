class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[]] * 2
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        answer[0] = (set_nums1 - set_nums2)
        answer[1] = (set_nums2 - set_nums1)
        return answer
        