"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    # Intuition
        # If meetings are sorted by their start time, then we only need to check adjacent meetings for overlap
        # By sorting once and doing a single pass, we can efficiently detect any conflict
    # Algorithm
        # 1. Sort all meetings by their start time.
        # 2. Iterate through the sorted list starting from the second meeting.
        # 3. For each pair of adjacent meetings:
            # let i1 be the previous meeting
            # let i2 be the current meeting
        # 4. If i1.end > i2.start:
            # the meetings overlap
            # return false
        # 5. If the loop finishes without finding any overlap:
            # return True
    # Time and Space Complexity
        # Time -> O(nlogn)
        # Space -> O(n)

        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True