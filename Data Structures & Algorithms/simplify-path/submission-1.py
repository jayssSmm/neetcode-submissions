class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        l = ['/']
        path = [i for i in path if i]
        for i in path:
            if i == '..':
                if len(l)>1 and l[-1] == '/':
                    l.pop()
                    l.pop()
                elif l[-1] != '/':
                    l.pop()
                
            elif i == '.':
                pass
            else:
                if l[-1] != '/':
                    l.append('/')
                l.append(i)
                print(l)
        print(l)
        if l[-1] == '/' and len(l)>1:
            l.pop()

        return ''.join(l)