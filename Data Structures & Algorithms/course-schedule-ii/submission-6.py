class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        bfs - Kahn's algorithm
        """
        pre_map = collections.defaultdict(list)
        in_deg = [0] * numCourses

        for crs, pre in prerequisites:
            pre_map[pre].append(crs)
            in_deg[crs] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)
            
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            for pre in pre_map[cur]:
                in_deg[pre] -= 1
                if in_deg[pre] == 0:
                    q.append(pre)
        return order if len(order) == numCourses else []


    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        not using visit, 
        topological sort
        """
        pre_map = collections.defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        cycle = set()
        result = []
        def dfs(i):
            if i in cycle:
                return False
            # this node is done
            if pre_map[i] is None:
                return True
            cycle.add(i)
            for pre in pre_map[i]:
                if not dfs(pre):
                    return False
            # mark the node is done + record this node
            cycle.remove(i)
            pre_map[i] = None
            result.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result

    def findOrder_og(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        pre_map = {
            1: 2
            2: [3, 4]
            3: [5]
            4: [3]
            5: []
        }
        [1,2,3,4,5]

        pre_map = {
        1: [0]
        }

        if cycle -> not able to
        """
        pre_map = collections.defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        cycle, visit = set(), set()
        result = []
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for pre in pre_map[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            visit.add(i)
            result.append(i)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return result