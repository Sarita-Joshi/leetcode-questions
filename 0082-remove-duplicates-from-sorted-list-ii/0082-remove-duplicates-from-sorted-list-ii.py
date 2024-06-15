# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # curr = head
#         data = []
#         dups = []
#         while curr:
#             if curr.val in data:
#                 dups.append(curr.val)
#             data.append(curr.val)
#             curr = curr.next
        
        dummy = ListNode(0,head)
        prev = dummy
        curr = prev.next
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                
            if prev.next== curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        
        return dummy.next
                
                
            