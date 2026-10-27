class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, speed] for  pos, speed in zip(position, speed)]
        cars.sort(reverse=True)
        stack = [(target - cars[0][0]) / cars[0][1]]
        for pos, speed in cars[1:]:
            time = (target - pos) / speed
            if time > stack[-1]:
                stack.append(time)
        return len(stack)