"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        one pass, using hashmap
        """
        map = collections.defaultdict(lambda: Node(0)) # use this to auto create a node
        map[None] = None
        cur = head
        while cur:
            map[cur].val = cur.val
            map[cur].next = map[cur.next] # this will create a node when it's not exist yet, then can assign the val later
            map[cur].random = map[cur.random]
            cur = cur.next
        return map[head]


        
        """
        two passes to solve, use hashmap to map the original node with new node, then link them with next and random
        3,7,4,5
        """
        map = {None: None}
        result = Node(0)
        ptr = head
        while ptr:
            node = Node(ptr.val)
            map[ptr] = node
            ptr = ptr.next
        

        ptr = head
        while ptr:
            node = map[ptr]
            next_node = map.get(ptr.next)
            random_node = map.get(ptr.random)
            node.next = next_node
            node.random = random_node
            ptr = ptr.next
        ptr = head
        return map[ptr]

        
        
