class Solution:
    def isValid(self, s: str) -> bool:
        i, size = 0, len(s)
        stack = []

        chars = {'(': ')', '{': '}', '[': ']'}
        while i < size:
            curr = s[i]
            if curr == ')' or curr == '}' or curr == ']':
                if len(stack) > 0:
                    comp = stack.pop()
                    print(chars[comp])
                    if curr != chars[comp]:
                        return False
                else:
                    return False
            else:
                stack.append(curr)
            i += 1
        return len(stack) == 0
