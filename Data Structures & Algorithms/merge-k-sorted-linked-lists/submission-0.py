# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge2lists(l1, l2):
            curr = dum = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next=  l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dum.next
        
        start = lists[0]
        for i in range(1, len(lists)):
            print(start, lists[i])
            start = merge2lists(start, lists[i])
        return start

                    