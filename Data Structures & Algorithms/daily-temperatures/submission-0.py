class Solution:

    #Iterate through the list backwards
    #First item (m = n-1), give score 0
    #Now add item to stack
    #Now go backwards
    #m-1
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if idx > 0:
                while stack and stack[-1][0] < temp:
                    curr = stack.pop()
                    res[curr[1]] = idx - curr[1]
            stack.append([temp, idx])
        return res
