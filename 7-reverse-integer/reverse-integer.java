class Solution 
{
    public int reverse(int x) 
    {
        double ans = 0;
	        int ans2 = 0;

	        if(x < -Math.pow(2,31) || x > Math.pow(2,31))
	        { return 0; }

	        String s = Integer.toString(Math.abs(x));

	        for(int i=s.length() ; i>0 ; i--)
	        {
                if(ans < Math.pow(2, 31))
	            {ans = ans + Integer.parseInt(Character.toString(s.charAt(i-1)))*Math.pow(10,(i-1));}
	        }

	        ans2 = (int)ans;
	    
            if(ans2 == 2147483647 || ans2 == -2147483647)
	        { return 0; }

            if(x<0)
	        { return -ans2; }
	        
	        return ans2;    
    }
}