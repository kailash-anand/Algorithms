class Solution {
    public String mergeAlternately(String word1, String word2) {
        boolean here = true;
        char[] appended = new char[word1.length() + word2.length()];
        int first = 0;
        int second = 0;
        int count = 0;

        while(first < word1.length() && second < word2.length())
        {
            if(here)
            {
                appended[count] = word1.charAt(first);
                count++;
                first++;
                here = false;
            }
            else
            {
                appended[count] = word2.charAt(second);
                count++;
                second++;
                here = true;
            }
        }

        while(first < word1.length())
        {
            appended[count] = word1.charAt(first);
            count++;
            first++;
        }

        while(second < word2.length())
        {
            appended[count] = word2.charAt(second);
            count++;
            second++;
        }

        return String.copyValueOf(appended);
    }
}