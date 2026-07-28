class Solution:
    def trap(self, height: List[int]) -> int:
        """
        improved 2nd
            [4,2,0,3,2,5]
    maxL     |
    maxR               |
            
        """
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        trapped = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trapped += maxL - height[l] if maxL - height[l] > 0 else 0
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trapped += maxR - height[r] if maxR - height[r] > 0 else 0
        return trapped



        """
        try 2nd:
        doc maxL & maxR
        each column, min(maxL, maxR) - height[i]
                     -> min(maxL, maxR) - height[current_step]

               [0,2,0,3,1,0,1,3,2,1]
          maxL  0,0,2,2,3,3,3,3,3,3
          maxR  3,3,3,3,3,3,3,2,1,0
min(maxL, maxR) 0,0,2,2,3,3,3,2,1,0
          res   0,0,2,0,2,3,2,0,0,0
        """
        maxL, maxR = [0] * len(height), [0] * len(height)
        cur_max = maxL[0]
        for i in range(len(maxL)):
            cur_max = max(cur_max, height[i])
            maxL[i] = cur_max

        cur_max = maxR[-1]
        for i in range(len(maxR) - 1, -1, -1):
            cur_max = max(cur_max, height[i])
            maxR[i] = cur_max
        
        min_res = [0] * len(height)
        for i in range(len(min_res)):
            min_res[i] = min(maxL[i], maxR[i])
        
        trapped = 0
        for i in range(len(height)):
            trapped += min_res[i] - height[i] if min_res[i] - height[i] > 0 else 0
        return trapped
        
















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

        """
        optimized, based on the maxLeft & maxRight, we actually don't need to know the exact max value of each side
        because what we need is the min value, so say left min is 2, no matter how big right side is, min is going to be 2


        if leftMax < rightMax: 
            res += leftMax - height[l] 
        else: res += rightMax - height[r] 
        is actually :
        res += min(leftMax, rightMax) - height[current_index]

        current_index is sometimes l, sometimes r
        moving around, bc we are checking either left, or right, by while l < r
        key[!the looping logic]: smaller val side check first
        """
        # optimize:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        trapped = 0
        while l < r:
            # [!the looping logic]: smaller val side check first

            # the left side is smaller -> which is the boundary
            if maxL < maxR: 
                l += 1
                maxL = max(maxL, height[l]) # find the current maxL
                trapped += maxL - height[l] # find how much water can trapped
                # don't need min(maxL, rightL), bc we already do that by (if maxL < maxR)
            # the right side is smaller -> which is the boundary
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trapped += maxR - height[r]
        return trapped



        # first try
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


        trapped = 0
        for k in range(len(height)):
            res = min(max_left[k], max_right[k]) - height[k]
            res = 0 if res < 0 else res
            trapped += res
        return trapped





