class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxi = 0
        while left < right:
            curr_height = min(height[left],height[right])
            curr_width = right - left
            curr_water = curr_height * curr_width
            maxi = max(maxi,curr_water)        
            if height[left] < height[right]:
                left+=1
            else:
                right -= 1
        return maxi