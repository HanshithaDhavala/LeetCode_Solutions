class Solution:

  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    remainder_counts = {}
    curr_sum = 0
    count = 0
    for num in nums:
      curr_sum += num
      rem = curr_sum % k
      if rem == 0:
        count += 1
      if rem in remainder_counts:
        count += remainder_counts[rem]
        remainder_counts[rem] += 1
      else:
        remainder_counts[rem] = 1
    return count