class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"*", "+", "-", "/"}:
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                if t == "*":
                    c = b * a
                elif t == "+":
                    c = b + a
                elif t == "/":
                    c = int(b / a) 
                elif t == "-":
                    c = b - a
                stack.append(c)
        return stack[-1]