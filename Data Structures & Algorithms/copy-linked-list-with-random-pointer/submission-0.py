"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        order = {}
        rev = {}
        curr = dummy = Node(0)
        while head:
            curr.next = Node(head.val)
            curr = curr.next
            order[curr] = head
            rev[head] = curr
            head = head.next
        
        curr = dummy.next
        while curr:
            t = order[curr]
            curr.random = rev.get(t.random)
            curr = curr.next
        return dummy.next
        
        
        
