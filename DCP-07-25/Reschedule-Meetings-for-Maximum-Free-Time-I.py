from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        total_meetings = len(startTime)
        total_busy = 0
        for idx in range(k):
            total_busy += endTime[idx]-startTime[idx]
        if total_meetings == k:
            return eventTime-total_busy
        max_free = startTime[k] - total_busy
        left = 0
        for right in range(k, total_meetings):
            total_busy += (endTime[right]-startTime[right])-(endTime[left]-startTime[left])
            next_start = eventTime if right == total_meetings-1 else startTime[right + 1]
            prev_end = endTime[left]
            max_free = max(max_free, next_start - prev_end - total_busy)
            left += 1
        return max_free