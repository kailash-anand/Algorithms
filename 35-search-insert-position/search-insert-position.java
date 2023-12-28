class Solution {
    public int searchInsert(int[] nums, int target) {
        if(target < nums[0])
        {
            return 0;
        }
        if(target > nums[nums.length-1])
        {
            return nums.length;
        }
        return binarySearch(nums,0,nums.length,target);
    }

    public int binarySearch(int[] arr, int start, int end, int target)
    {
        int middle = (start + end)/2;

        if(arr[middle] == target)
        {
            return middle;
        }

        if(Math.abs(start-end) == 1)
        {
            return middle+1;
        }

        if(target < arr[middle])
        {
            return binarySearch(arr, start, middle, target);
        }
        else
        {
            return binarySearch(arr, middle, end, target);
        }
    }
}