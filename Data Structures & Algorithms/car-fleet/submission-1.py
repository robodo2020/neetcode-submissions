class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position = [4,1,0,7]
        speed =    [2,2,1,1]
        t = 1      [6,3,1,8]
        t = 2      [8,5,2,9]
        t = 3      [10,7,3,10]
        t = 4      [x,9,4,x]
        
        position = [7,4,1,0]
        speed    = [1,2,2,1]
        times    = [3,3,4,5,10]
        cur_max_time -> see if any can catch it
        constraints: not able to pass the front car
        return num of car fleets (group together) 

        at any timing before target, car distance is the same, drive min of their speed, as a fleet
        """
        cars = sorted(zip(position, speed), reverse=True)
        cur_max = 0 
        fleets = 0
        for position, speed in cars:
            t = (target - position) / speed
            if t > cur_max:
                fleets += 1
                cur_max = t
        return fleets




