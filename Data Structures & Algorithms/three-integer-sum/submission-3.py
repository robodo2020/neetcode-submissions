class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-4,-1,-1,0,1,2]
         |
            |
                      |
        """
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif val > 0:
                    k -= 1
                else:
                    j += 1
        return list(res)