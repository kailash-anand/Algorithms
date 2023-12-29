class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;
        int count = 0;
        int longest = 0;
        boolean noOnes = true;

        while(right < nums.length)
        {
            if(nums[right] == 0)
            {
                count++;
            }
            else
            {
                noOnes = false;
            }

            while(count > k)
            {
                if(nums[left] == 0)
                {
                    count--;
                }
                left++;
            }

            if(right - left > longest)
            {
                longest = right - left;
            }

            right++;
        }

        if(noOnes && k == 0)
        {
            return longest;
        }
        return longest + 1;
    }
}