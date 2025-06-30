class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
            
        Max = 0
        for num in count:
            if num+1 in count:
                curr = count[num] + count[num+1]
                Max = max(Max,curr)
        return Max