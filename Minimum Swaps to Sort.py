
class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        #Code here
        posd = { x:i for i, x in enumerate(nums)}

        ends = sorted(nums)

        ans = 0
    
        for i, v in enumerate(ends):
    
            oi = posd[v]
    
            if oi != i:
    
                posd[nums[i]] = oi
    
                ans+=1
    
                nums[oi], nums[i] = nums[i], nums[oi]
    
        return ans
#{ 
#  Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)

# } Driver Code Ends