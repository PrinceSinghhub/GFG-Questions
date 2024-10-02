class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        # Code here
        product_till_now = 1
        sub_count = 0
        ptr = 0
        total = 0

        for i in range(n):

            # we compute product_till_now and increment our sub count

            product_till_now *= a[i]
            sub_count += 1

            # if our product becomes greater than k
            # we move out ptr and take out the nums[ptr] from product till now

            while product_till_now >= k and ptr <= i:
                product_till_now /= a[ptr]
                ptr += 1
                sub_count -= 1

            total += sub_count
        return total

    # {


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]

        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends