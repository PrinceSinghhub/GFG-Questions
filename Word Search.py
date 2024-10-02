'''
//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
public:
    bool solve(int i,int j,int n,int m,int k,string s,
    vector<vector<char>>board){

        if(k==s.size()){
            return true;
        }

        if(i<0 or j<0 or i>=n or j>=m or board[i][j]!=s[k]){
            return false;
        }

        board[i][j]='#';

        return (solve(i-1,j,n,m,k+1,s,board) or solve(i,j-1,n,m,k+1,s,board ) or
               solve(i+1,j,n,m,k+1,s,board) or solve(i,j+1,n,m,k+1,s,board));

    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<char>>board(n, vector<char>(m, '*'));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> board[i][j];
		string word;
		cin >> word;
		Solution obj;
		bool ans = obj.isWordExist(board, word);
		if(ans)
			cout << "1\n";
		else cout << "0\n";
	}
	return 0;
}
// } Driver Code Ends
'''