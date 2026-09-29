# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            if not head: return None

            curr, prev = head, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev, head
        
        start = end = head
        prev = dummy = ListNode(0,head)

        while start and end:
            i=0
            while end and i<k-1:
                end = end.next
                i+=1
            if not end:
                break
            next = end.next #starting of next group
            end.next=None
            newstart, newend = reverse(start)
            prev.next= newstart
            newend.next = next
            prev = newend
            start = end = next
        return dummy.next

