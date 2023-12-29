class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0;
        int right = 0;
        int count = 0;
        int longest = 0;

        while (right < nums.length) {
            if (nums[right] == 0) {
                count++;
            }

            while (count > 1) {
                if (nums[left] == 0) {
                    count--;
                }
                left++;
            }

            longest = Math.max(longest, right - left);

            right++;
        }

        return longest;
    }
}
