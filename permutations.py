"""
https://leetcode.com/problems/permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
def permute(nums):
  res = []
  if not nums:
    return [[]]
  def dfs(v, subArr, temp):
    temp.append(v)
    if not subArr:
      res.append(temp)
    if len(subArr) == 2:
      #add unswapped
      res.append(temp + subArr)
      #swap
      subArr[0], subArr[1] = subArr[1], subArr[0]
      #add swapped
      res.append(temp + subArr)
      return
    for i, v in enumerate(subArr):
      dfs(v, subArr[:i] + subArr[i+1:], temp[:])

  for i in range(len(nums)):
    dfs(nums[i], nums[:i] + nums[i+1:], [])
  
  return res
print(permute([1,2,3]))
# print(permute([1]))




      
    
    