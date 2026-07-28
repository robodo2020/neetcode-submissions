# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast & slow ptr
        """
        1->2->3->4
              |
           |
        remember to walk through an example, good behavior for debug & also prove concept is correct
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

        # set solution
        visited = set()
        ptr = head
        while ptr:
            node = ptr
            if node in visited:
                return True
            visited.add(node)
            ptr = ptr.next
        return False
        