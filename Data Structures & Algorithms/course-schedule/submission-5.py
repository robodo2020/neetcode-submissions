class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            find if there's any cycle
            0: 1

            visited: 0
        """
        
        pre_map = collections.defaultdict(list)

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if pre_map[i] == []:
                return True
            visited.add(i)
            pres = pre_map.get(i, [])
            for pre in pres:
                if not dfs(pre):
                    return False
            visited.remove(i)
            pre_map[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

            


