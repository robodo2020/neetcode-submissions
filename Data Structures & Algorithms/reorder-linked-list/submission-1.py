# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. find the middle point
        2. reverse the second
        3. merge two lists
        [0, 1, 2, 3, 4, 5, 6]
                           |
                  |
        0,1,2,3
        slow = 4,5,6

            4,5,6
ptr         |
tmp:          |

        0,1,2,3
        |
        6,5,4
        |
        """
        # find the middle point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # cut the first, and reverse the second
        second = slow.next # the second list
        slow.next = None # separate the first & second
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge 2 lists
        """
          0,1,2,3
     l1   |
     tmp1   |
          6,5,4
     l2   |
     tmp2   |
        """
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2 # already swapped, so need to redirect to tmp
        







