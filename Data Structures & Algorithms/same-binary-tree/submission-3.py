# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        traverse and the same time, if any time is different, return false

        BFS to traverse, any time find a differences, return False directly
        """
        qp = deque([p])
        qq = deque([q])

        while qp and qq:
            node_p = qp.popleft()
            node_q = qq.popleft()

            if node_p == node_q == None:
                continue
            if node_p is None or node_q is None:
                return False
            if node_p.val != node_q.val:
                return False
            
            qp.append(node_p.left)
            qp.append(node_p.right)
            qq.append(node_q.left)
            qq.append(node_q.right)
        return len(qp) == len(qq) == 0

    
    def isSameTree_first_try(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        traverse and the same time, if any time is different, return false

        BFS to traverse, any time find a differences, return False directly
        even tho it's None case should add in as well

        this is okay but has potential bug if queue_p & queue_q has different num of nodes
        """

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p or queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()
            if (node_p and node_q): # both has val case
                if node_p.val != node_q.val:
                    return False
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)
            elif node_p == node_q == None:
                continue
            else:
                return False
        return True
            