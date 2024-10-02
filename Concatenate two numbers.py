class Solution:
    def countPairs(self, N, X, numbers):
       #code here
       l = len(str(X))
       s_x = str(X)

       #Step 1
       dic = {(0,i):0 for i in range(l-1)}
       for i in range(1, l):
           dic[(i,l-1)] = 0

        #step 2
       for num in numbers:
           s_num = str(num)
           if len(s_num) >= l:
               continue
           if s_x[:len(s_num)] == s_num:
               dic[(0,len(s_num)-1)] += 1
           if s_x[l-len(s_num):] == s_num:
               dic[(l-len(s_num),l-1)] += 1
       count = 0

        #step 3
       for i in range(0, l-1):
           if l%2 == 0 and (l//2)-1 == i:
               if s_x[:i+1] == s_x[i+1:]:
                   count += (dic[(0,i)] * (dic[(i+1, l-1)]-1))
               else:
                   count += (dic[(0,i)] * dic[(i+1, l-1)])
           else:
               count += (dic[(0,i)] * dic[(i+1, l-1)])
       return count



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)
