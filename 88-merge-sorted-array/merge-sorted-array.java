import java.util.*;
class Solution 
{
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {      
        int temp = 0; 
        for(int j=0 ; j<n ; j++)
        {
            nums1[m+j] = nums2[j];
        }

        Arrays.sort(nums1);
    }
}