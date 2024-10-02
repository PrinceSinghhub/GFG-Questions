''''
//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

#include <vector>
#include <algorithm>

class Solution {
public:
    int min_operations(std::vector<int>& nums) {
        int n = nums.size();
        int lis = 1;
        std::vector<int> dp(n, 1);
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j] && (nums[i] - nums[j]) >= (i - j)) {
                    dp[i] = std::max(1 + dp[j], dp[i]);
                    lis = std::max(lis, dp[i]);
                }
            }
        }
        return (n - lis);
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
            cin >> nums[i];
        Solution ob;
        int ans = ob.min_operations(nums);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends'''