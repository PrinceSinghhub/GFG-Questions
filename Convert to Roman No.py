
class Solution:
    def convertRoman(self,n):
        arr = [[5000, 'V'],[4000, 'XV'],[3000, 'MMM'],[2000, 'MM'],[1000, 'M'],[900, 'CM'],[500, 'D'],[400, 'CD'],[100, 'C'],[90, 'XC'],[50, 'L'],[40, 'XL'],[10, 'X'], [9, 'IX'], [8, 'VIII'],[7, 'VII'],[6,'VI'],[5,'V'], [4,'IV'], [3,'III'],[2, 'II'],[1, 'I']]
        s= ''
        a = 0
        while n!=0:
            for i in range (len(arr)):
                if n>=arr[i][0] :
                    s +=arr[i][1]
                    n-= arr[i][0]
                    break
        return s

#{
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends