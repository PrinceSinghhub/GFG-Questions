'''
class Solution
{
    //Function to find the smallest positive number missing from the array.
    static int missingNumber(int arr[], int size)
    {
        Arrays.sort(arr);
        int temp = 0;
        for(int i : arr){
            if(i == temp + 1){
                temp += 1;
            }
        }
        return temp+1;
    }
}

'''
