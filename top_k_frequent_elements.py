"""
https://leetcode.com/problems/top-k-frequent-elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
"""

#step 1: keep count of integers, store in a dict: counter!
#step 2: make a heap?
#step 3: turn heap into array?

from collections import Counter
import heapq

def topKFrequent(nums, k):
    c = Counter(nums) #dict with counts of integer appearances
    
    hp = []
    for key, val in c.items():
        heapq.heappush(hp, (val, key))
   
    return [i[1] for i in heapq.nlargest(k, hp)]

print(topKFrequent([], 0))
print(topKFrequent([-1, -1], 1))
print(topKFrequent([1], 1))
print(topKFrequent([1,1,1,2,2,3], 2))


