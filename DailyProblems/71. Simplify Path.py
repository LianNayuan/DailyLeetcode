class Solution:
    def simplifyPath(self, path: str) -> str:
        unix_paths = path.split('/')
        a = []
        for unix_path in unix_paths:
            if unix_path not in ['','.','..']:
                a.append(unix_path)
            elif unix_path == '..' and a:
                a.pop()
        return "/" + "/".join(a)
