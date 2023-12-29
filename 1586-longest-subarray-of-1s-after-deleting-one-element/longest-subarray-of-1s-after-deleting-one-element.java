class Solution {
    public int longestSubarray(int[] nums) 
    {
        int left = 0;
        int right = 0;
        int count = 0;
        int longest = 0;

        while (right < nums.length) 
        {
            if (nums[right] == 0) 
            {
                count++;
            }

            if(count == 2)
            {
                while(nums[left] != 0)
                {
                    left++;
                }
                left++;
                count = 1;
            }

            if(right - left > longest)
            {
                longest = right - left;
            }

            right++;
        }

        return longest;
    }
}
