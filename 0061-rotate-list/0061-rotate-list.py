# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head:
            return head
        
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        
        rot = count - (k % count)
        if rot == count:
            return head
        
        curr = head
        for _ in range(rot-1):
            curr = curr.next
        new_head = curr.next
        
        curr.next = None
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        return new_head