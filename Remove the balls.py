from typing import List


class Solution:
    def finLength(self, N: int, color: List[int], radius: List[int]) -> int:
        # code here

        colr = []
        rds = []

        colr.append(color[0])
        rds.append(radius[0])

        for i in range(1, N):

            print(colr)
            print(rds)

            if len(colr) != 0 and len(rds) != 0:
                if color[i] == colr[-1] and radius[i] == rds[-1]:
                    colr.pop()
                    rds.pop()

                else:
                    colr.append(color[i])
                    rds.append(radius[i])
            else:
                colr.append(color[i])
                rds.append(radius[i])

        return len(rds)

ans = Solution()
N = 10
color = [1,2,2,2,2,6,7,8,9,9]
radius = [1,2,2,2,2,6,7,8,9,9]
print(ans.finLength(N,color,radius))