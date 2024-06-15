# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack= []
        
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
            
        for i in range(n-1):
            curr = stack.pop()
            
        remove = stack.pop()
        if stack:
            prev= stack.pop()
            prev.next = curr
        else:
            head = curr
        return head