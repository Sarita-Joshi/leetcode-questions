# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        
        def reverse(start, end):
            
            stack = []
            while start!=end:
                stack.append(start)
                start = start.next
            while stack:
                start.next = stack.pop()
                start = start.next
            return end, start
        
        
        dummy = None
        curr = dummy
        start, end = None, None
        count = k
        while head:
            count-=1
            if count==k-1:
                start = head
                head = head.next

            elif count == 0:
                end = head
                head = head.next
                start, end = reverse(start, end)
                if not dummy:
                    dummy = start
                else:
                    curr.next = start
                curr = end
                curr.next = head
                count = k
            else:
                head = head.next
        
        return dummy
                    
                
            
                
            
                