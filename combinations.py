"""
https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Constraints:
    1 <= n <= 20
    1 <= k <= n
 

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""
'''
def dfs( parameter ):

	if stop condtion or base case:
		# base case:
		update result
	    return
	
	else:
		# general cases:
		for all possible next moves:
		
		    select one next move
			dfs( paramter with selected next move )
			undo the selection
	
		return
'''
def combine(n, k):
    res = []
    numArr = [i for i in range(1, n+1)]

    def dfs(num, arr, temp):
        temp.append(num)
        if len(temp) == k:
            res.append(temp)
            return
        for i, v in enumerate(arr):
            dfs(v, arr[i+1:], temp[:])

    for i in range(n):
        dfs(numArr[i], numArr[i+1:], [])
    
    return res

print(combine(5, 3))





