'''
//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int minTime(int S1, int S2, int N){
       // code here
       int min_val = INT_MAX;
       int temp;
       if(S1 > S2){
             temp = S1;
               S1 = S2;
               S2 = temp;
       }
       for(int i=1;i<=N;i++){
           int ans = max(S1*i,S2*(N-i));
           min_val = min(min_val,ans);
       }
       return min_val;
   }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int S1, S2, N;
        cin>>S1>>S2>>N;

        Solution ob;
        cout<<ob.minTime(S1, S2, N)<<"\n";
    }
    return 0;
}
// } Driver Code Ends

'''