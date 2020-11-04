"""
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

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

def reverseList(head):
    if not head or not head.next:
        return head
    
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p





linkedList1 = LinkedList([1,2,3,4,5])

