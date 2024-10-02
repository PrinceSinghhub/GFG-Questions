# using bit magic
class Solution:
    def findPosition(self, N):
        # code here
        if N==0 or N&(N-1)!=0:
            return -1
        count=0
        while N!=0:
            N=N>>1
            count+=1
        return count

# normal approch
class Solution1:
    def findPosition(self, N):

        Bin = bin(N)[2::]

        if Bin.count('1') > 1:
            return -1

        if '1' not in Bin:
            return -1

        count = 0

        for i in Bin[::-1]:
            if i == '1':
                return count + 1
            else:
                count += 1

        return count