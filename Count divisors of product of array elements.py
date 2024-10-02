#User function Template for python3

class Solution:
    def countDivisorsMult(self, a, n):
        
        
        pro = 1
        for i in a:
            pro*=i
        
        
        ans = []
        
        for i in range(1,pro+1):
            
            if pro%i == 0:
                ans.append(i)
        return len(ans)

# optimize code
class Solution:
   def countDivisorsMult(self, a, n):
       #Code here
       prod = 1
       for i in range(len(a)):
           prod *= a[i]
       p = 2
       prime = []
       while prod!=1:
           if prod%p == 0:
               prod //=p
               prime.append(p)
               continue
           p += 1
       d = {i:prime.count(i) for i in prime}
       No_of_factors = 1
       for key,value in d.items():
           No_of_factors *= (1+value)
       return No_of_factors
    
    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        print(Solution().countDivisorsMult(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends