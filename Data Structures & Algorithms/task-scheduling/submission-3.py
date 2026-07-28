class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        
        max_heap: take the cur max count element
        queue: the cool down element (cool_time)
        """
        map = {}
        for task in tasks:
            map[task] = 1 + map.get(task, 0)
        
        heap = []
        for cnt in map.values():
            heapq.heappush(heap, -cnt)
        queue = collections.deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    queue.append((task, time + n))
            if queue:
                if time == queue[0][1]:
                    task, _ = queue.popleft()
                    heapq.heappush(heap, task)
            
            
        return time



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
            # check if the first node finished the cooldon, if so, put it back to queue
            if queue:
                cool_time = queue[0][1]
                if cool_time == time:
                    count, cool_time = queue.popleft()
                    heapq.heappush(max_heap, count)
        return time
        """
        old notes:
        tasks = ["A","A","A","B","B","B"], n = 2 (cool down period)
            maxHeap[-3] queue[[cd, count]]
                            [3,-2]
            1 + n 



            tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2

            1. count the num of elements, put into heap
            2. maintain minHeap for next job, queue for cool down 
            3. while heap or queue still has value
                3.1 if minHeap has value, means there's still job, pop it out and if not 0, put into job count
                3.2 if cool down queue has value, check whether the current job is ready for uses by the time
                heap = [-int] queue = [[cd, jobCount]]
        """
