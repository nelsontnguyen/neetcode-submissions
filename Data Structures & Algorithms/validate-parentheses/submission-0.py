class Solution:
    def isValid(self, s: str) -> bool:
        # we first need to define a dictionary with keys and values

        dct = {")":"(", "}": "{", "]":"["}

        # this problem uses a stack
        stack = []

        for c in s:
            if c in dct:
                if stack and stack[-1] == dct[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            