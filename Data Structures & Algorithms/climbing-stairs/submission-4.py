class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n+1)

        def climb(step_num, n, steps):
            if steps[step_num] == 0:
                if step_num >= n-1:
                    steps[step_num] = 1
                else:
                    steps[step_num] = steps[step_num+1] + steps[step_num+2]
            
            if step_num == 0:
                return steps[step_num]
            return climb(step_num-1, n, steps)

        res = climb(n, n, steps)
        print(steps)
        return res