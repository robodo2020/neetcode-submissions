class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            brute force
            sorting solution
            store count of each value
            sort by count
            return
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
