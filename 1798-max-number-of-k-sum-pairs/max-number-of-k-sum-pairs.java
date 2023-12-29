class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums); // Sort the array
        int sum = 0;
        int maxOperations = 0;
        int left = 0;
        int right = nums.length - 1;

        while (left < right) 
        {
            sum = nums[left] + nums[right];
            if (sum == k) 
            {
                maxOperations++;
                left++;
                right--;
            } 
            else if (sum < k) 
            {
                left++;
            } 
            else 
            {
                right--;
            }
        }

        return maxOperations;
    }
}

