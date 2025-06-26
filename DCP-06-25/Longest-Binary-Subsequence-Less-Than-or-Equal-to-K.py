class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        result = ''
        for i in range(len(s)-1,-1,-1):
            base2 = int(s[i] + result, 2)
            if base2 <= k:
                result = s[i] + result 
        return len(result)