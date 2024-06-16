# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        start = ListNode()
        end = start
        parts = start
        curr = head
        
        while curr:
            if end==start:
                end.next = ListNode(curr.val)
                end = end.next
                
                if curr.val < x:
                    parts = parts.next
                
            elif curr.val >= x:
                end.next = ListNode(curr.val)
                end = end.next
                
                if curr.val < x:
                    parts = parts.next
            else:
                parts.next = ListNode(curr.val, parts.next)
                if parts==end:
                    end = end.next
                parts = parts.next
                
            
            curr = curr.next
            
        return start.next