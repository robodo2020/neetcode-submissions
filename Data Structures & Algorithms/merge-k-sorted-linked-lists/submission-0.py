# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        having k ptrs, each round find the min of 3 ptrs, if found, move it's pointer
        [1,2,4]
             |
        [1,3,5]
           |
        [6,8]
         |
        1,1,2
        """
        res = ListNode(0)
        ptr = res
        while (any(n is not None for n in lists)):
            vals = []
            for node in lists:
                if node:
                    vals.append(node.val)
            cur_min = min(vals)

            for i in range(len(lists)):
                if lists[i] and lists[i].val == cur_min:
                    ptr.next = ListNode(cur_min)
                    ptr = ptr.next
                    lists[i] = lists[i].next
        return res.next
                    

        


        