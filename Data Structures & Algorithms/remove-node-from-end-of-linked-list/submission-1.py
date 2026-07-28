# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1. get the len of the list
        2. have another ptr traverse to the removed node
        3. remove it
        [1,2,3,4,5] n = 2

        """
        len = 0
        ptr = head
        while ptr:
            len += 1
            ptr = ptr.next
        
        target = len - n
        if target == 0:
            return head.next
        
        ptr = head
        for _ in range(target - 1):
            ptr = ptr.next
        ptr.next = ptr.next.next

        return head

        