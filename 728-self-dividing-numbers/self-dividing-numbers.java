class Solution 
{
    public List<Integer> selfDividingNumbers(int left, int right) 
    {
        List<Integer> selfDividingNums = new ArrayList<>();

        for(int i = left; i <= right; i++)
        {
            if(isSelfDividing(i))
            {
                selfDividingNums.add(i);
            }
        }

        return selfDividingNums;
    }

    public boolean isSelfDividing(int num)
    {
        String number = "" + num;

        for(int i = 0; i < number.length(); i++)
        {
            int current = number.charAt(i) - '0';
            if((current == 0) || ((num % current) != 0))
            {
                return false;
            }
        }

        return true;
    }
}