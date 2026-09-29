class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  
        times = []

        for i, n in enumerate(position):
            times.append((target -  n)/speed[i])
        
        position = sorted(zip(position, times))
        for i in range(len(position) -1, -1, -1):
            if not stack:
                stack.append(position[i][1])

            if stack[-1] < position[i][-1]:
                stack.append(position[i][1])

            else:
                continue

        return len(stack)
            