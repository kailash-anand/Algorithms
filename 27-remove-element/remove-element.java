class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for(int i=0 ; i<nums.length ; i++)
        {
            if(nums[i] == val)
            {
                int count = nums.length - 1;
                while(nums[count] == val && count > i)
                {
                    count--;
                }
                if(count != i)
                {
                    swap(nums, i, count);
                    k++;
                }
                else
                {
                    break;
                }
            }
            else
            {
                k++;
            }
        }
        return k;
    }

    public void swap(int[] arr, int index1, int index2)
    {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}