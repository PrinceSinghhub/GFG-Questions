class Solution:
    def changeBits(self, N):
       z=bin(N)[2:]
       s=""
       for i in range(len(z)):
           s+="1"
       m=int(s,2)
       l=[]
       l.append(m-N)
       l.append(m)
       return l