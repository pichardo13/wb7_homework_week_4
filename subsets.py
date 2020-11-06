"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def subsets(nums):
    subs = [[nums[0]]]
    for i in range(1, len(nums)):
        temp = []
        for s in subs:
            temp.append(s[:] + [nums[i]])
        subs.append([nums[i]])
        subs += temp[:]
    subs.append([])
    return subs
    


print(subsets([1,2,3]))