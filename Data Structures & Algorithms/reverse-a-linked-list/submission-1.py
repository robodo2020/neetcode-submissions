# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            0-1-2-3
    curr    | nxt
    prev  |
      None
        having two pointers
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr     # move the pointers to the next item
            curr = nxt      # move the pointers to the next item
        return prev

        