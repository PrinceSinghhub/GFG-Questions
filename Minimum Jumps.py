'''


class Solution
{
    static int minJumps(int[] arr)
    {
        int i=0;
        int n = arr.length;
        int hops=0;

        if(n==1) return 0;


        while(i<n-1)
        {
            if(arr[i]==0) return -1;

            int maxInd = i+1;

            if(i+arr[i]>=n-1) return hops+1;

            for(int j=i+1; j<n && j<=i+arr[i]; j++)
            {
                if(arr[maxInd]+maxInd<arr[j]+j) maxInd = j;
            }

            i = maxInd;

            hops++;
        }

        return hops;

    }
}

'''