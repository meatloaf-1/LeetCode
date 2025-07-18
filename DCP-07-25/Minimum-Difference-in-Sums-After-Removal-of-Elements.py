import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        left_sum = sum(nums[:n])
        right_sum = sum(nums[-n:])
        
        left_heap = [-x for x in nums[:n]]
        heapq.heapify(left_heap)
        left_sums = [left_sum]
        curr_sum = left_sum
        
        for i in range(n, 2 * n):
            heapq.heappush(left_heap, -nums[i])
            curr_sum += nums[i] + heapq.heappop(left_heap)
            left_sums.append(curr_sum)
        
        right_heap = nums[-n:]
        heapq.heapify(right_heap)
        right_sums = [right_sum]
        curr_sum = right_sum
        
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            curr_sum += nums[i] - heapq.heappop(right_heap)
            right_sums.append(curr_sum)
        
        right_sums = right_sums[::-1]
        min_diff = float('inf')
        for l, r in zip(left_sums, right_sums):
            min_diff = min(min_diff, l - r)
        return min_diff