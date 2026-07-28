class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        [1,3,4,2,2]
        Floyd's cycle detection
        integer in range [1, n]
        turn index, val to Node(key, next)
        0->1->2<->3, meaning has cycle, and to find the answer, need to know the entrance of the cycle (which is 2)
        """

        # this only ensures they slow & fast meeting each other in the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # this is to ensure finding the entrance, Floyd algorithm
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
