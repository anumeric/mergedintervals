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
            # IF OVERLAP EXISTS
            # 1. set temp = overlap
            # 2. update last entry in res with the overlap
            if isOverlap(res[-1],intervals[i]): # overlap 
                minStart = min(res[-1][0],intervals[i][0])
                maxFinish = max(res[-1][1],intervals[i][1])
                #temp = [minStart,maxFinish]
                res[-1] = [minStart,maxFinish]
                
            # IF NO OVERLAP EXISTS
            # 1. set temp = current interval 
            # 2. add current interval to res
            else:
                #temp = [intervals[i][0],intervals[i][1]]
                res.append([intervals[i][0],intervals[i][1]]) # current interval 

        return res
