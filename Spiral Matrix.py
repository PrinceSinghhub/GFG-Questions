class Solution:
    def findK(self, a, n, m, k):
       # Your code goes here
       ans=[]
       left=0
       right=m-1
       up=0
       down=n-1
       c=0
       while(len(ans)<n*m):
           for i in range(left,right+1):
               c+=1
               ans.append(a[up][i])
               if c==k:
                   return ans[c-1]
           for j in range(up+1,down+1):
               c+=1
               ans.append(a[j][right])
               if c==k:
                   return ans[c-1]
           if up!=down:
               for i in range(right-1,left-1,-1):
                   c+=1
                   ans.append(a[down][i])
                   if c==k:
                       return ans[c-1]
           if left!=right:
               for i in range(down-1,up,-1):
                   c+=1
                   ans.append(a[i][left])
                   if c==k:
                       return ans[c-1]
           up+=1
           right-=1
           down-=1
           left+=1
       return ans[k-1]



#{
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends