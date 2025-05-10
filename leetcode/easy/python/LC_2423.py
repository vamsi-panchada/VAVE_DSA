from collections import defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = defaultdict(int)
        for i in word:
            counter[i] += 1
        
        # counter = {"a": 1, "b": 1, "c": 2}
        frequencies = list(counter.values())
        
        for i in range(len(frequencies)):
            frequencies[i] -= 1
            if len(set(frequencies)) == 1:
                return True
            # Case: were counter = {"a": 1, "b": 2, "c": 2}
            if frequencies[i] == 0 and len(set(frequencies)) == 2:
                return True
            frequencies[i] += 1
        
        return False

solution = Solution()
word = input()
print(solution.equalFrequency(word))