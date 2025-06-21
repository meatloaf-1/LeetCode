class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        b = sorted(Counter(word).values())
        return min(sum(b[:i])+sum(max(v-b[i]-k,0) for v in b[i:]) for i in range(len(b))) 