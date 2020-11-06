"""
https://leetcode.com/problems/merge-k-sorted-lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4
"""
import heapq
# class LinkedList:
#     def __init__(self, lists = None):
#         self.head = ListNode()
#         self.lastNode = self.head.next

#         if lists:
#             self.addItems(lists)


#     def addItems(self, lists):
#         curr = self.head
#         for i in lists:
#             curr.val = i
#             curr.next = ListNode()
#             self.lastNode = curr.next
#             curr = curr.next
    
#     def add(self, item):
#         curr = self.head
#         while curr.val and curr.next:
#             curr = curr.next
#         curr.val = LinkedList(item)
        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addItems(items):
    linkedList = ListNode(items[0])
    curr = linkedList.next
    for i in items[1:]:
        curr = ListNode(i)
        curr = curr.next
    return linkedList

def mergeKLists(lists):
    h = []
    for linkedList in lists:
        curr = linkedList
        while curr.val:
            heapq.heappush(h, curr.val)
            curr = curr.next
    
    items = [heapq.heappop(h) for i in range(len(h))]
    return addItems(items)

# linkedList1 = LinkedList([1,4,5])
# linkedList2 = LinkedList([1,3,4])
# linkedList3 = LinkedList([2,6])

linkedList1 = ListNode(1, ListNode(4, ListNode(5)))
linkedList2 = ListNode(1, ListNode(3, ListNode(4)))
linkedList3 = ListNode(2, ListNode(6))

mergeKLists([linkedList1, linkedList2, linkedList3])
mergeKLists([])