# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev = None
        post = None
        stack = []
        i=1
        curr = head
        while curr and i< right + 1:
            print(i, curr.val)
            if i==left-1 and left!=1:
                prev = curr
            elif left <= i <= right:
                stack.append(curr)
            
            curr = curr.next
            i+=1
        
        post = curr
        if not prev or left==1:
            head = prev = stack.pop()    
        while stack:
            prev.next = stack.pop()
            prev = prev.next

        prev.next = post
        
        return head
                
            
        
        
                
                
            