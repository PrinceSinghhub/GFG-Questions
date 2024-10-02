import collections

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        map=collections.defaultdict(int)
        for i in range(N):
            if bills[i]==5:
                map[bills[i]]+=1
            elif bills[i]==10:
                map[bills[i]]+=1
                if map[5]>0:
                    map[5]-=1
                else:
                    return False
            else:
                map[bills[i]]+=1
                if map[5]>0 and map[10]>0:
                    map[5]-=1
                    map[10]-=1
                elif map[5]>=3:
                    map[5]-=3
                else:
                    return False
        return True