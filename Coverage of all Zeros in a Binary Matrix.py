'''

//{ Driver Code Starts


#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends




class Solution {
public:
    int FindCoverage(vector<vector<int>>&v){
        int res=0;

        for(int i=0;i<v.size();i++){

            for(int j=0;j<v[0].size();j++){

                if(v[i][j]==0){

                    //first  row
                if(i!=0 && v[i-1][j]==1)
                    res++;

                //last row
                if(i != v.size()-1 && v[i+1][j]==1)
                    res++;

                //first col
                if(j !=0 && v[i][j-1]==1)
                    res++;

                //last col
                if(j != v[0].size()-1 && v[i][j+1]==1)
                    res++;
                }

        }

        }
        return res;
    }

};





//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> matrix[i][j];
        Solution obj;
        int ans = obj.findCoverage(matrix);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends

'''