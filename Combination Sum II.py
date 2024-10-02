'''
//User function Template for C++

class Solution{
public:
void solve(int ind,int target,vector<int>& ar,vector<int>& temp,vector<vector<int>>& ans){
        if(target==0){
            ans.push_back(temp);
            return;
        }
        for(int i=ind;i<ar.size();i++){
            if(i>ind && ar[i]==ar[i-1]) continue;
            if(ar[i]>target) break;
            temp.push_back(ar[i]);
            solve(i+1,target-ar[i],ar,temp,ans);
            temp.pop_back();
        }
    }
    vector<vector<int>> CombinationSum2(vector<int> arr,int n,int k)
    {
        sort(arr.begin(),arr.end());
        vector<vector<int>>ans;
        vector<int>v;
        int index=0;
        solve(index,k,arr,v,ans);
        return ans;
        //code here
    }
};

'''