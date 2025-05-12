from typing import List
from collections import defaultdict, deque

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def get_component(node):
            queue = deque([node])
            component = []
            visited[node] = True
            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return component

        cycles = []
        linked = []
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                component = get_component(node)
                if all(len(graph[i]) == 2 for i in component):
                    cycles.append(len(component))
                elif len(component) > 1:
                    linked.append(len(component))

        def calc(l, r, is_cycle):
            d = deque([r, r])
            res = 0
            for a in range(r - 1, l - 1, -1):
                v = d.popleft()
                res += v * a
                d.append(a)
            return res + d[0] * d[1] * is_cycle

        res = 0
        linked = sorted(linked, reverse=True)
        for k in cycles:
            res += calc(n - k + 1, n, 1)
            n -= k
        for k in linked:
            res += calc(n - k + 1, n, 0)
            n -= k

        return res


solution = Solution()
n = int(input())
edges = eval(input())
print(solution.maxScore(n=n, edges=edges))