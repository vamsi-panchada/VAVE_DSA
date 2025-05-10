class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)

        parts = p.split("*")
        prefix, sufix = parts[0], parts[1]

        prefix_len, sufix_len = len(prefix), len(sufix)

        prefix_found = True if prefix_len == 0 else False
        sufix_found = True if sufix_len == 0 else False

        idx = 0

        while not prefix_found and idx <= n-prefix_len:
            if s[idx: idx+prefix_len] == prefix:
                prefix_found = True
                idx += idx+prefix_len
            else:
                idx += 1

        while prefix_found and idx <= n-sufix_len:
            if s[idx: idx+sufix_len] == sufix:
                sufix_found = True
                break
            idx += 1
        
        return prefix_found and sufix_found

solution = Solution()
s = input()
p = input()
print("true" if solution.hasMatch(s=s, p=p) else "false")