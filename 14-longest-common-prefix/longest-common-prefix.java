class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        String prefix = "";
        int min = strs[0].length(),i = 0;
        boolean check = true;

        for(int j = 1 ; j < strs.length ; j++)
        {
            if(strs[j].length() < min )
            { min = strs[j].length(); }
        }

        for(int j = 0 ; j < min ; j++)
        {
            for( i=0 ; i< strs.length-1 ; i++)
            {
                if(strs[i].charAt(j) != strs[i+1].charAt(j))
                {
                    check = false;
                    break;
                }
            }
            if(check)
            { prefix = prefix + strs[i].charAt(j); }
        }
        return prefix;
    }
}