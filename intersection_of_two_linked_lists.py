"""
https://leetcode.com/problems/intersection-of-two-linked-lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists: begin to intersect at node c1.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists 
intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B. 

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the 
intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists 
do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, lst = None):
        self.head = ListNode()
        curr = self.head
        if lst:
            for i in lst:
                curr.val = i
                curr.next = ListNode()
                curr = curr.next

def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    
    hA, aCount = headA, 0
    hB, bCount = headB, 0

    while hA:
        aCount += 1
        hA = hA.next
    
    while hB:
        bCount += 1
        hB = hB.next
    
    if aCount > bCount:
        for i in range(aCount - bCount):
            headA = headA.next
    elif bCount > aCount:
        for i in range(bCount - aCount):
            headB = headB.next
    
    while headA and headB:
        if headA == headB:
            return headA
    return None

# listA = [4,1,8,4,5] 
# listB = [5,6,1,8,4,5]

listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]

linkedA = LinkedList(listA)
linkedB = LinkedList(listB)
print(getIntersectionNode(linkedA.head, linkedB.head))

# listA = [4,1,8,4,5]
# listB = [5,6,1,8,4,5]