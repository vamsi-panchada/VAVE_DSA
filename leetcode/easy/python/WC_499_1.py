from collections import defaultdict
import heapq

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        for i in s:
            counter[i] += 1
        if len(counter)<=k:
            return 0
        smallest = heapq.nsmallest(len(counter) - k, counter.values())
        return sum(smallest)


solution = Solution()
s = input()
k = int(input())
print(solution.minDeletion(s=s, k=k))