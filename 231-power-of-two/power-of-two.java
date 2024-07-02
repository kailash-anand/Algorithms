class Solution {
    public boolean isPowerOfTwo(int n) 
    {
        if(n == 0)
        {
            return false;
        }

        double result = Math.log(n)/Math.log(2);
        int resultToInt = (int)result;

        if(Math.pow(2, resultToInt) == n)
        {
            return true;
        }

        return false;
    }
}