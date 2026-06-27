class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        first = 0
        second = 0
        for t in tokens:
            if t in operators and stack:
                first = stack.pop()
                second = stack.pop()
                if t == "+":
                    first = second + first
                elif t == "-":
                    first = second - first
                elif t == "*":
                    first = second * first
                elif t == "/":
                    first = second / first
                    if first < 0:
                        first = math.ceil(first)
                    else:
                        first = math.floor(first)
                stack.append(first)
            else:
                stack.append(int(t))
            print(stack)
        return stack.pop()
                