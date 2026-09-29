# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head :
            return

        
        slow , fast= head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        curr = second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #new head of second half
        first, second = head, prev

        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        
        

        


        


        #merge two
        

