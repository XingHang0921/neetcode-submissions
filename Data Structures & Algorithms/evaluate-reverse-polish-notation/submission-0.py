class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in '+-*/':
                s.append(int(t))
            else:
                b = s.pop()  # right operand
                a = s.pop()  # left operand
                if t == '+':
                    s.append(a + b)
                elif t == '-':
                    s.append(a - b)
                elif t == '*':
                    s.append(a * b)
                elif t == '/':
                    s.append(int(a / b))  # truncates toward zero

        return s[0]