# https://leetcode.com/problems/two-sum/

from typing import List 

def twoSum(nums: List[int], target: int) -> bool:
    nums.sort()
    l = 0 
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return True
    return False

nums = [2,7,11,15, 8] 
target = 9
result = twoSum(nums, target=target)
print(result)
