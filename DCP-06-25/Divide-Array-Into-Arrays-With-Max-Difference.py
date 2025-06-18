class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range (0, len(nums), 3):
            if nums[i] + k >= nums[i+2]:
                result.append(nums[i:i+3])
            else:
                return []
        return result