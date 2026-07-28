# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        heap optimized
        initialize the heap with the first value of each list
        pop the first node out of the heap
        when put the first node val to the result, push the next node back to the heap
        """
        heap = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        dummy = ListNode(0)
        ptr = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1 # just to avoid internal error of heap trying to compare node.val if it's same val
        return dummy.next


        """
        heap solution
        TC:
            O(m) m = number of nodes
        SC:
            O(2m) 
        """
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        res = ListNode(0)
        ptr = res
        while heap:
            val = heapq.heappop(heap)
            ptr.next = ListNode(val)
            ptr = ptr.next
        return res.next





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
                    

        


        