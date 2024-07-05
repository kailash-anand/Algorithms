class Solution {
    public String toGoatLatin(String sentence) 
    {
        final String VOWELS = "aeiouAEIOU";
        String a = "a";

        String[] words = sentence.split(" ");
        String goatWord = "";

        for(int i = 0; i < words.length; i++)
        {
            if(VOWELS.contains(String.valueOf(words[i].charAt(0))))
            {
                words[i] += "ma";
            }
            else
            {
                char first = words[i].charAt(0);
                words[i] = words[i].substring(1) + first + "ma";
            }

            words[i] += a;
            a += "a";
        }

        for(int i = 0; i < words.length; i++)
        {
            if(i == words.length - 1)
            {
                goatWord += words[i];
            } 
            else
            {
                goatWord += words[i] + " ";
            }
        }

        return goatWord;
    }
}