# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        ptr = head
        while ptr:
            node = ptr
            if node in visited:
                return True
            visited.add(node)
            ptr = ptr.next
        return False
        