class Solution 
{
    public int[] findErrorNums(int[] nums) 
    {
        int duplicate = 0;
        int[] resultArr = new int[2];
        int missing = 0;
        int actSum = 0;
        int expSum = (nums.length*(nums.length+1))/2;

        Arrays.sort(nums);

        for(int i = 0; i < (nums.length - 1); i++)
        {
            actSum += nums[i];
            if(nums[i] == nums[i+1])
            {
                duplicate = nums[i];
            }
        }
        actSum += nums[nums.length-1];

        missing = (expSum - actSum) + duplicate;

        resultArr[0] = duplicate;
        resultArr[1] = missing;

        return resultArr;
    }
}