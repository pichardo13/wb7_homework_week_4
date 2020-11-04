"""
https://leetcode.com/problems/reverse-linked-list-ii
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


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

def reverseBetween(head, m, n) :
        if not head:
            return
        
        
        i = m - 1
        h = node = ListNode(None)
        node.next = head
        while i > 0:
            node = node.next
            i -= 1
        
        node.next = reverse(node.next, n - m + 1)

        while h.next is not None:
            print(h.val)
            h = h.next
        return h.next

def reverse(node, length):
            head = node
            _next = prev = None
            i = 0
            while i < length:
                i += 1
                _next = node.next
                node.next = prev
                prev = node
                node = _next
            
            head.next = node
            return prev

linkedList = LinkedList([1,2,3,4,5])
reverseBetween(linkedList.head, 2, 4)