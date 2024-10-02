# The Same Solution Gives TLE thats why we conver into the CPP


'''
//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++
#include <iostream>
#include <vector>

class Solution {
public:

    bool checkAllStars(const std::string& str1, int index1) {
        for (int i = 1; i <= index1; ++i) {
            if (str1[i-1] != '*') {
                return false;
            }
        }
        return true;
    }

    bool spaceOptimizationApproach(int index1, int index2, const std::string& str1, const std::string& str2, std::vector<bool>& prev, std::vector<bool>& curr) {
        // All the Base Cases
        prev[0] = true;

        for (int indx1 = 1; indx1 <= index1; ++indx1) {
            // Special Case when the index2 < 0 it means we want all the str1 char is "*"
            curr[0] = checkAllStars(str1, indx1);

            for (int indx2 = 1; indx2 <= index2; ++indx2) {
                if (str1[indx1-1] == str2[indx2-1] || str1[indx1-1] == '?') {
                    curr[indx2] = prev[indx2-1];
                } else if (str1[indx1-1] == '*') {
                    bool ignoreStar = prev[indx2];
                    bool compareWithStar = curr[indx2-1];
                    curr[indx2] = ignoreStar || compareWithStar;
                } else {
                    curr[indx2] = false;
                }
            }

            // Copy values from curr to prev for the next iteration
            prev = curr;
        }

        return prev[index2];
    }

    bool match(const std::string& str1, const std::string& str2) {
        int n = str1.length();
        int m = str2.length();
        std::vector<bool> prev(m+1, false);
        std::vector<bool> curr(m+1, false);

        return spaceOptimizationApproach(n, m, str1, str2, prev, curr);
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t-->0)
    {
        string wild, pattern;
        cin>>wild>>pattern;

        Solution ob;
        bool x=ob.match(wild, pattern);
        if(x)
        cout<<"Yes\n";
        else
        cout<<"No\n";
    }
    return 0;
}
// } Driver Code Ends
'''