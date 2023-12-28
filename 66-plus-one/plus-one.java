class Solution {
    public int[] plusOne(int[] digits) {
        		  int count = 0;

	        if(digits.length == 1 && digits[0] == 9 )
			{
	            int[] arr = {1,0};
				return arr;
			}
			 
			if(digits[digits.length-1] != 9)
			{
				digits[digits.length-1] = digits[digits.length-1] + 1;
			}
			else
			{
	            for(int i=0 ; i<digits.length ; i++)
	            {
	                if(digits[digits.length-1-i] == 9)
	                { count++;}
	                else
	                { break; }
	            }
	            if(count == digits.length)
	            {
	            	int[] arr = new int[digits.length+1];
	            	arr[0] = 1;
	            	for(int i=1 ; i<arr.length ; i++)
	            	{
	            		arr[i] = 0;	            		
	            	}	            	
	            	return arr;
	            }
	            
	            
	            for(int i=0 ; i<count ; i++)
	            {
	                digits[digits.length-1-i] = 0;
	            }
				
				digits[digits.length-1-count] = digits[digits.length-1-count] + 1;
			}
			
			return digits;
    }
}