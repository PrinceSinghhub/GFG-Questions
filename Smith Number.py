'''


//User function Template for Java

class Solution {
    static int smithNum(int n) {
        // code here
        int sum=0;
        int k=n;
        int temp=digitSum(n);
        for(int i=2;i<=Math.sqrt(n);i++){
            while(n%i==0){
                sum+=digitSum(i);
                n/=i;
            }
        }
        if(n>1 && n!=k){
            sum+=digitSum(n);
        }

        return sum==temp?1:0;
    }
    static int digitSum(int n){
        int temp=n;
        int ans=0;
        while(temp!=0){
            ans+=temp%10;
            temp/=10;
        }
        return ans;
    }
};
'''