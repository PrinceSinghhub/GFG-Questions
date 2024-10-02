import collections
from typing import List
class unionfind:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    def find(self,x):
        while x != self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,x1,x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return  False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2]+=self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = unionfind(len(accounts))
        emailtoaccount = {}
        for index ,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailtoaccount:
                    uf.union(index,emailtoaccount[email])
                else:
                    emailtoaccount[email] = index
        emailgroup = collections.defaultdict(list)
        for email,index in emailtoaccount.items():
            leader = uf.find(index)
            emailgroup[leader].append(email)
        res = []
        for index,email in emailgroup.items():
            name = accounts[index][0]
            res.append([name]+sorted(emailgroup[index]))
        return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends