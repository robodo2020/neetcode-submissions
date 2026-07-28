# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        original solution optimized with dummynode
        "A dummy node eliminates special cases by guarantee that every real node has a previous node"
        can eliminate edge cases

        d,1,2,3,4
                | -> 4
            |
        """
        dummy = ListNode(0, head)
        ptr = dummy
        len = 0
        while ptr.next:
            len += 1
            ptr = ptr.next
        target = len - n
        ptr = dummy
        for _ in range(target):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return dummy.next

        




        """
        idea 2:
        two pointer, first move n node, then bring the second node to the right place
        having a dummy node to make the traverse easier
        d,1,2,3,4
                |
            |
        """
        dummy = ListNode(0, head)
        left = right = dummy
        for _ in range(n):
            right = right.next
        
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next

        """
        original solution:
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

        