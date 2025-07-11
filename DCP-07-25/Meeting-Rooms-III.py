import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avl = list(range(n))
        heapq.heapify(avl)
        ongoing = []
        count = [0] * n

        for start, end in meetings:
            while ongoing and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(avl, room)
            if avl:
                room = heapq.heappop(avl)
                heapq.heappush(ongoing, (end, room))
                count[room] += 1
            else:
                earliest_end, room = heapq.heappop(ongoing)
                duration = end - start
                heapq.heappush(ongoing, (earliest_end + duration, room))
                count[room] += 1

        max_meetings = max(count)
        return count.index(max_meetings)