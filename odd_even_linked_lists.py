"""
https://leetcode.com/problems/odd-even-linked-list/
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Constraints:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].
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

    def print(self):
        while self.head.next is not None:
            print(self.head.val)
            self.head = self.head.next

    def oddEvenLists(self):
        if self.head is None:
            return None
        
        odd = self.head
        even = self.head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return self.head
    

linkedList = LinkedList([1,2,3,4,5])
linkedList.oddEvenLists()
linkedList.print()