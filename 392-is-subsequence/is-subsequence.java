class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() > t.length())
        {
            return false;
        }
        if(s.equals(""))
        {
            return true;
        }

        int firstIndex = 0;
        int secondIndex = 0;

        while(secondIndex < t.length())
        {
            if(s.charAt(firstIndex) == t.charAt(secondIndex))
            {
                firstIndex++;
            }

            if(firstIndex == s.length())
            {
                return true;
            }

            secondIndex++;
        }

        return false;
    }
}