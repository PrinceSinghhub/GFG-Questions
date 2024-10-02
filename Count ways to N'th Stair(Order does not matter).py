'''



class Solution
{
    public long nthStair(int n)

    {

        // Code here

        long res[]=new long[n+1];

        res[0]=0;

        res[1]=1;

        int i=2;int j=2;

        while(i<n+1){

            res[i]=j;

            if(i+1<=n)

            res[i+1]=j;

            j++;

            i=i+2;

        }

        return res[n];

    }
}

'''