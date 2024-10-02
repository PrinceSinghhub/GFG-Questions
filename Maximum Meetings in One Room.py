from typing import List


class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        temp = [((F[i], S[i]), i + 1) for i in range(N)]
        temp.sort()

        ans = [temp[0][1]]
        finalTime = temp[0][0][0]

        for i in range(1, N):
            if temp[i][0][1] > finalTime:
                ans.append(temp[i][1])
                finalTime = temp[i][0][0]

        ans.sort()
        return ans
