class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengths = [1] 
        for op in operations:
            lengths.append(lengths[-1] * 2)

        def dfs(i, k):
            if i == 0:
                return 'a'

            half = lengths[i] // 2
            if k <= half:
                return dfs(i - 1, k)
            else:
                ch = dfs(i - 1, k - half)
                if operations[i - 1] == 0:
                    return ch
                else:
                    return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))

        return dfs(len(operations), k)