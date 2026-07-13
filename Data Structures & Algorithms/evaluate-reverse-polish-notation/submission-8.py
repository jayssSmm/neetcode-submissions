class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+', '-', '*', '/']
        l=[]

        for i in tokens:
            if i not in signs:
                l.append(int(i))
            else:
                x=l.pop()
                y=l.pop()

                match i:
                    case '+':
                        l.append(y+x)
                    case '-':
                        l.append(y-x)
                    case '*':
                        l.append(y*x)
                    case '/':
                        l.append(int(y/x))

        return (l.pop())