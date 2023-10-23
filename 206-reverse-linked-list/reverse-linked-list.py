# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        None   1 -> 2 -> 3 -> 4 -> 5 -> null
        p      c
            
        None <- 1 -> 2 - 3 - 4 - 5
                pc
        
        -1 <- 1 -> 2 - 3 - 4 - 5
              pc
        """
        curr = head
        prev = None

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev