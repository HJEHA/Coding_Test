# https://leetcode.com/problems/two-sum/

from typing import List 

def twoSum(nums: List[int], target: int) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

nums = [2,7,11,15] 
target = 9
result = twoSum(nums, target=target)
print(result)
