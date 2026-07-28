class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        invariant:
        sort the position in descending order
        1. All cars in idex < i, already form some number of fleets, that won't interact with the car that idx > i
        2. cur_max_time: current max arrival time (slowest, cars will prob catch it up)
        3. if current car's arrival time t <= cur_max_time, meaning it will catch up, form a fleet
        4. else (t > cur_max_time), will be a new fleet, update the cur_max_time
        """
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        cur_max_time = 0
        for p, s in cars:
            time = (target - p) / s
            if cur_max_time < time:
                res += 1
                cur_max_time = time
        return res





