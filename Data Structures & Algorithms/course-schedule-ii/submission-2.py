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
        visiting, cycle = set(), set()
        output = []
        pre_map = collections.defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(i):
            if i in cycle:
                return False
            # not pretty sure why this is return True directly, need to check
            if i in visiting:
                return True
            pres = pre_map[i]
            cycle.add(i)
            for pre in pres:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            visiting.add(i)
            output.append(i)

            return True

        for i in range(numCourses):
            res = dfs(i)
            if not res:
                return []

        return output

