class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # The key strategies for this problem involve sorting, iterating backwards
        cars = [(p, s) for p,s in zip(position, speed)]
        cars.sort(key=lambda car: car[0])

        # Working backwards, determine when each car is scheduled to reach the destination
        stack = []
        for i in range(len(cars)-1, -1, -1):
            # ex: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
            # this becomes [0,1,4,7], [1,2,2,1]
            # 7 will take 3 seconds: 7+1+1+1
            # (target-pos) / speed
            car_position, car_speed = cars[i]
            arrival_time = (target-car_position) / car_speed
            if stack and arrival_time <= stack[-1][0]:
                stack[-1][1].append(car_position)
            else:
                stack.append((arrival_time, [car_position]))
        return len(stack)