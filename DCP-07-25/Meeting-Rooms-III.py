import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)
        ongoing = []
        count = [0] * n

        for start, end in meetings:
            while ongoing and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                heapq.heappush(ongoing, (end, room))
                count[room] += 1
            else:
                earliest_end, room = heapq.heappop(ongoing)
                duration = end - start
                heapq.heappush(ongoing, (earliest_end + duration, room))
                count[room] += 1

        max_meetings = max(count)
        return count.index(max_meetings)