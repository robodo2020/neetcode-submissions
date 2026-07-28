class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        cycle = set()
        visit = set()
        start_cycle = -1
        def dfs(cur, par):
            nonlocal start_cycle
            if cur in visit:
                start_cycle = cur
                return True
            
            visit.add(cur)
            for nxt in graph[cur]:
                if nxt == par:
                    continue
                if dfs(nxt, cur):
                    if start_cycle != -1:
                        cycle.add(cur)
                    if cur == start_cycle:
                        start_cycle = -1
                    return True
            
            return False


        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
























    def findRedundantConnection_og(self, edges: List[List[int]]) -> List[int]:
        """
        if find cycle: mean the path to the cycle can be removed
        og solution: find the cycle, append all visited node back to path, then find the last edge
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
        for x, y in reversed(edges):
            if (x, y) in visit_edges or (y, x) in visit_edges:
                return [x, y]



