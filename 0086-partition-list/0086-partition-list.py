# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, curr: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        big = ListNode(0)
        small = ListNode(0)
        bigcurr = big
        smallcurr = small
        while curr:
            
            if curr.val >= x:
                bigcurr.next = ListNode(curr.val)
                bigcurr = bigcurr.next
                
                if curr.val < x:
                    parts = parts.next
            else:
                smallcurr.next = ListNode(curr.val)
                smallcurr = smallcurr.next
            
            curr = curr.next
            
        smallcurr.next = big.next
            
        return small.next