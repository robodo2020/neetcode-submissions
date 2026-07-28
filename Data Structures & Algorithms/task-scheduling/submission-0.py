class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        A:3
        B:1
        C:1
        
        A: 3, 0
        B: 1, 0
        C: 1, 0

        queue -> like a cache, store the tasks still in cooldown
        max_heap -> always with the available tasks
        """
        map = {}
        for task in tasks:
            map[task] = 1 + map.get(task, 0)
        
        max_heap = [-cnt for cnt in map.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = collections.deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    queue.append([count, time + n])
            if queue:
                cool_time = queue[0][1]
                if cool_time == time:
                    count, cool_time = queue.popleft()
                    heapq.heappush(max_heap, count)
        return time

