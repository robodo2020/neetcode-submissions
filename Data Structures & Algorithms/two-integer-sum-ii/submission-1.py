class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l + 1, r + 1]
            if res > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]

        """
        TODO: other solution
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]