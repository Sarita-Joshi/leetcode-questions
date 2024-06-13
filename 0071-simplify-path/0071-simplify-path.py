class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path)==1:
            return path
        
        path= path.strip('/').split('/')
        dirs = []
        for i in path:

            if i == '' or i=='.':
                continue
            if i == '..':
                if len(dirs):
                    dirs.pop()
            else:
                dirs.append(i)
        
        return '/'+ '/'.join(dirs)