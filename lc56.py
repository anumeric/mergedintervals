class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(a,b):
            maxStart = max(a[0],b[0])
            minFinish = min(a[1],b[1])
            return (minFinish >=  maxStart) # overlap
        
        intervals.sort()
        res = []
        temp = intervals[0]
        res.append(temp)
        
        for i in range(1,len(intervals)):
            if isOverlap(temp,intervals[i]): # overlap 
                minStart = min(temp[0],intervals[i][0])
                maxFinish = max(temp[1],intervals[i][1])
                temp = [minStart,maxFinish]
                res[-1] = temp
            else:
                temp = [intervals[i][0],intervals[i][1]]
                res.append(temp)
        return res
