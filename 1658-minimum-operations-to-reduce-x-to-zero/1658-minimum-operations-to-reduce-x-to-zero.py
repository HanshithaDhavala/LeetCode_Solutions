class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        current_sum = 0
        max_len = -1
        left = 0     
        for right in range(len(nums)):
            current_sum += nums[right]
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
        if max_len != -1:
            return len(nums) - max_len
        else:
            return -1