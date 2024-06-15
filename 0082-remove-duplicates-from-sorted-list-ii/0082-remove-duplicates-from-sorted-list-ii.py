# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        data = set()
        dups = set()
        while curr:
            if curr.val in data:
                dups.add(curr.val)
            data.add(curr.val)
            curr = curr.next
        
        dummy = ListNode(0,head)
        prev = dummy
        curr = prev.next
        while curr:
            if curr.val not in dups:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        
        prev.next = curr
        
        return dummy.next
                
                
            