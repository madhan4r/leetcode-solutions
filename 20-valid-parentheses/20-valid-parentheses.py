class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for p in s:
            if p in paranthesis:
                stack.append(p)
            else:
                if not stack:
                    return False
                if paranthesis[stack.pop()] != p:
                    return False
        return False if stack else True
        