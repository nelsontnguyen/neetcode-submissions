class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif token == "-":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(b - a)
            elif token == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif token == "/":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(int(float(b) / a))
            else:
                num_stack.append(int(token))
            
        return num_stack[0]
        