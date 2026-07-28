class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            minHeap
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        """
            brute force
            sorting solution
            store count of each value
            sort by count
            return

            TC: O(nlogn) on sort
            SC: O(3n) = O(n)
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        for _ in range(k):
            cnt, num = arr.pop()
            res.append(num)
        return res
