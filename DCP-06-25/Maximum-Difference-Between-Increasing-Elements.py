class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        mina = nums[0]

        for i in range(1, len(nums)):
            result = max(result, nums[i] - mina)
            mina = min(mina, nums[i])
        
        if result == 0:
            return -1
        else:
            return result