class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n=len(s)
        for i in range (0, n, k):
            grp = s[i:i+k]
            if len(grp) < k:
                grp += fill*(k - len(grp))
            res.append(grp)
        return res