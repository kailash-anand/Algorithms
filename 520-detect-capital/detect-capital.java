class Solution {
    public boolean detectCapitalUse(String word) 
    {
        if(Character.isLowerCase(word.charAt(0)))
        {
            if(word.equals(word.toLowerCase()))
            {
                return true;
            }
        }
        else
        {
            if(word.equals(word.toUpperCase()))
            {
                return true;
            }

            String wordWithoutFirstChar = word.substring(1);
            if(wordWithoutFirstChar.equals((wordWithoutFirstChar).toLowerCase()))
            {
                return true;
            }
        }

        return false;
    }
}