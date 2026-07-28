class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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