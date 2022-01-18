class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def trans(s):
            return int(s[0:2])*60 + int(s[3:5])
        minute = []
        for timePoint in timePoints:
            time = trans(timePoint)
            minute.append(time)
        minute.sort()
        minute.append(1440+minute[0])
        dif = []
        for i in range(len(minute)-1):
            dif.append(minute[i+1] - minute[i])
        return min(dif)
