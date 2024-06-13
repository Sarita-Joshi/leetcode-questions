class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path)==1:
            return path
        
        path= re.sub('//+', "/", path).strip('/').split('/')
        dirs = []
        for i in path:

            if i=='.':
                continue
            elif i == '..':
                if dirs:
                    dirs.pop()
            else:
                dirs.append(i)
        
        return '/'+ '/'.join(dirs)