class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_even = False
        has_odd = False
        min_val = nums1[0]  
        for x in nums1:
            if x % 2 == 0:
                has_even = True
            else:
                has_odd = True  
            if x < min_val:
                min_val = x
        # Purely even or purely odd array
        if not (has_even and has_odd):
            return True
        # Mixed parities require an odd minimum
        return min_val % 2 != 0