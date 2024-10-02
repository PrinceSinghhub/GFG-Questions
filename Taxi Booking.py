class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        a=[]
        for i in range(0, N):
            a.append(time[i]*(abs(cur-pos[i])))
        return min(a) 