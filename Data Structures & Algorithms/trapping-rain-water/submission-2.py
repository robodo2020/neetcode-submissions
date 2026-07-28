class Solution:
    def trap(self, height: List[int]) -> int:
        """
        min(L, R) - h[i]
        use each column to calculate how much water can trap
        [0,2,0,3,1,0,1,3,2,1]
         |
         min(l, r) - h[i] = 0 - 0 = 0
           |
           min(l, r) - h[i] = min(0, 3) - 2 = -2 -> 0
             |
             min(2, 3) - 0 = 2 - 0 = 2
               |
               min(0, 3) - 3 -> 0
                  |
                  min(3, 3) - 1 = 2

          [0,2,0,3,1,0,1,3,2,1]
  maxLeft  0,0,2,2,3,3,3,3,3,3 (loop from left to right)
 maxRight  3,3,3,3,3,3,3,2,1,0 (loop from right to left)
min(L, R)  0,0,2,2,3,3,3,2,1,0


        [4,2,0,3,2,5]
         0,4,4,4,4,4
         5,5,5,5,5,0
         0,4,4,4,4,0
 trapped 0,2,4,1,2,0
        """
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_res = [0] * len(height)
        cur_max = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], cur_max)
            cur_max = max(cur_max, height[i])
        
        cur_max = height[-1]
        for j in range(len(height) - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], cur_max)
            cur_max = max(cur_max, height[j])
        print(max_left)
        print(max_right)
        trapped = 0
        for k in range(len(height)):
            res = min(max_left[k], max_right[k]) - height[k]
            res = 0 if res < 0 else res
            trapped += res
        return trapped





