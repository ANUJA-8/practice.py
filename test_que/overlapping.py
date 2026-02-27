# Maximum Number of Non-Overlapping Intervals
# Two intervals are considered non-overlapping if one interval ends before or exactly when the other interval begins.
# Input:start = [1, 3, 5, 7] end= [2, 4, 6, 8]
# Intervals:[1,2], [3,4], [5,6], [7,8]
# Output:4

class Intervals:
    def maxinterval(start,end):
        count=0
        for i in range(0,len(start)-1):
            for j in range(0,len(end)-1):
                if end[j]== start[i+1] or start[i+1]== end[j]+1:
                    count+=2
                else:
                    count+=1
            return count
                    
# start=[1, 3, 5, 7]
# end=[2, 4, 6, 8]
start = [3,4,5]
end   = [5,9,8]
print(Intervals.maxinterval(start,end))
                    