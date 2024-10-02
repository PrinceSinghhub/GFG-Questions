'''
//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            int a = sc.nextInt();
            long b = sc.nextLong();

            Solution ob = new Solution();
            System.out.println(ob.power(a, b));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static long power(int a, long b){

        //complete the function here

        long h= 1000000007;

          if(b < 1){

           return 1;

       }



      long  hp= power(a,b/2);

      long res  = 1;

      if(b % 2 == 0){

          res *= (hp) % h * (hp) % h;

      }else{

          res *= (hp) % h * (hp) % h * a;

      }

       return res % h;



    }
}

'''