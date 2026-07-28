# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        6->7->8
        |
        7->8->9
        |
        3->6->8->1

        """
        res = ListNode(0)
        ptr = res

        plus = 0
        while l1 or l2:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next 

            sum = val1 + val2 + plus
            plus = 0
            if sum >= 10:
                sum -= 10
                plus = 1
            node = ListNode(sum)
            ptr.next = node
            ptr = ptr.next

        if plus == 1:
            node = ListNode(plus)        
            ptr.next = node
        return res.next

