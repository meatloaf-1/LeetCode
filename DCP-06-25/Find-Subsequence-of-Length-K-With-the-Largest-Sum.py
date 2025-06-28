class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        index=sorted([(num,i) for i, num in enumerate(nums)])
        return [num for num, i in sorted(index[-k :], key=lambda x: x[1])]