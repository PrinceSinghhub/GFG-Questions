#User function Template for python3
class Solution:
	def baseEquiv(self, n, m):
	    def dec_to_base(num,base):  
            base_num = ""
            while num>0:
                dig = int(num%base)
                if dig<10:
                    base_num += str(dig)
                else:
                    base_num += chr(ord('A')+dig-10) 
                num //= base
            base_num = base_num[::-1]
            return base_num

        for i in range(2,33):
            ans=dec_to_base(n,i)
            
            if len(ans)==m:
                return "Yes"
        
        return "No"



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends