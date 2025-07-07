import heapq

class Solution:
    def maxEvents(self,events):
        events.sort()
        total_days = max(end for _, end in events)
        i = 0
        n = len(events)
        event_heap = []
        attended = 0

        for day in range(1, total_days + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(event_heap, events[i][1])
                i += 1

            while event_heap and event_heap[0] < day:
                heapq.heappop(event_heap)

            if event_heap:
                heapq.heappop(event_heap)
                attended += 1

        return attended