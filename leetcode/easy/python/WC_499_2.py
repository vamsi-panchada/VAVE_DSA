from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        horizontal_sum = [sum(i) for i in grid]
        verical_sum = [sum(i) for i in zip(*grid)]
        def can_partition(sums: List[int]) -> bool:
            total = sum(sums)
            prefix = 0
            for value in sums[:-1]:
                prefix += value
                if prefix * 2 == total:
                    return True
            return False
        return can_partition(horizontal_sum) or can_partition(verical_sum)

solution = Solution()
grid = eval(input())
print("true" if solution.canPartitionGrid(grid=grid) else "false")