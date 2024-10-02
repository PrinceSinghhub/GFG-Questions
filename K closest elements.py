'''

class Solution {
    int binarySearch(int arr[],int x){
        int lo = 0,hi = arr.length-1;
        while(lo <= hi){
            int mid = (lo + hi)/2;
            if(arr[mid]==x)return mid;
            else if(arr[mid]>x)hi = mid - 1;
            else lo = mid + 1;
        }
        return hi;
    }
    int[] printKClosest(int[] arr, int n, int k, int x) {
        int getIndex=binarySearch(arr,x);
        int i;
        if(getIndex!=-1 && getIndex!=n && arr[getIndex]==x)
        i = getIndex - 1;
        else i = getIndex;
        int j = getIndex+1;
        List<Integer> ls=new ArrayList<>();
        for(int t=0;t<k;t++){
            int first = i>=0?Math.abs(arr[i]-x):Integer.MAX_VALUE;
            int second = j<arr.length?Math.abs(arr[j]-x):Integer.MAX_VALUE;
            if(first<second){
                ls.add(arr[i]);
                i--;
            }else {
                ls.add(arr[j]);
                j++;
            }
        }
        int nums[]=new int[ls.size()];
        for(i=0;i<ls.size();i++)
        nums[i]=ls.get(i);
        return nums;
    }
}

'''