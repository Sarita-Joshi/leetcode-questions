# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr = res
        carry = 0
        while l1 and l2:
            k = l1.val + l2.val + carry
            if k > 9:
                carry = k // 10
                k = k % 10
            else:
                carry = 0
            curr.next = ListNode(val=k)
            curr = curr.next
            l1= l1.next
            l2= l2.next
        
        while l1:
            k = l1.val + carry
            if k > 9:
                carry = k // 10
                k = k % 10
            else:
                carry = 0
            curr.next = ListNode(val=k)
            curr = curr.next
            l1= l1.next
        
        while l2:
            k = l2.val + carry
            if k > 9:
                carry = k // 10
                k = k % 10
            else:
                carry = 0
            curr.next = ListNode(val=k)
            curr = curr.next
            l2= l2.next
        
        if carry!=0:
            curr.next = ListNode(val=carry)
            curr = curr.next
        
        return res.next
            
            
            
            
                