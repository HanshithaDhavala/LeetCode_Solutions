class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # 1. If all elements are already even or all are odd
        if all(x % 2 == 0 for x in nums1) or all(x % 2 != 0 for x in nums1):
            return True
        return min(nums1) % 2 != 0