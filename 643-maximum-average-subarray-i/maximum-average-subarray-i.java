class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int left = 0;
        int right = k -1;
        double sum = 0;

        for(int i=0 ; i<k ; i++)
        {
            sum += nums[i];
        }

        double temp = sum;
        while(right < nums.length)
        {
            temp -= nums[left];
            left++;
            right++;

            if(right == nums.length)
            { break;} 

            temp += nums[right];

            if(temp > sum)
            {
                sum = temp;
            }
        }

        return sum/k;
    }
}