'''
//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    vector<long long> smallerSum(int n,vector<int> &arr){


        vector<long long>dublicate;
        for(auto i:arr){
            dublicate.push_back(i);
        }

        sort(arr.begin(), arr.end());
        long long Sum = arr[0];
        vector<long long>pair{0,arr[0]};

        map<long long,long long>pairIndex;

        pairIndex[arr[0]] = 0;


        for(int i = 1; i < arr.size(); i++){

            if(pair[1] == arr[i]){
                pairIndex[arr[i]] = pair[0];
                Sum+=arr[i];
            }
            else{
                pairIndex[arr[i]] = Sum;
                pair[0] = Sum;
                pair[1] = arr[i];
                Sum+=arr[i];
            }


        }

        vector<long long> ans;
        for(int i = 0; i < arr.size(); i++){
            long long val = pairIndex[dublicate[i]];
            ans.push_back(val);

        }


        return ans;


}
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        Solution ob;
        vector<long long> ans=ob.smallerSum(n,arr);
        for(int i=0;i<n;i++){
            if(i!=n-1){
                cout<<ans[i]<<" ";
            }
            else{
                cout<<ans[i]<<endl;
            }
        }
    }
    return 0;
}
// } Driver Code Ends

'''