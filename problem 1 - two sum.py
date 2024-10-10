# @title problem 1: Two Sum
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            difference = target - num
            print(difference)
            for j, num in enumerate(nums):
              if j!=i and num == difference:
                return [i, j]



nums = [2,7,11,15]
target = 9
solution = Solution()
solution.twoSum(nums, target)

