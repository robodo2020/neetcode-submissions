class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        if find cycle: mean the path to the cycle can be removed
        """

        mapping = collections.defaultdict(list)
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        
        visit_edges = set()
        visit_node = []
        self.find_cycle = False
            
        def dfs(cur, pre):
            if cur in visit_node:
                pre = cur
                for node in reversed(visit_node):
                    visit_edges.add((node, pre))
                    pre = node
                    if node == cur:
                        break
                self.find_cycle = True
                return

            
            visit_node.append(cur)
            for nxt in mapping[cur]:
                if nxt == pre:
                    continue
                if not self.find_cycle:
                    dfs(nxt, cur)
            visit_node.remove(cur)
            return 
        dfs(1, 0)
        print(visit_edges)
        for x, y in reversed(edges):
            if (x, y) in visit_edges or (y, x) in visit_edges:
                return [x, y]



