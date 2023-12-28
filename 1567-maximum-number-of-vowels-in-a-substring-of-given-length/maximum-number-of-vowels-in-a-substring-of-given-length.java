class Solution {
    public int maxVowels(String s, int k) {
        int numberOfVowels = 0;
        int length = s.length();
        int first = 0;
        int last = k - 1;
        int count = 0;

        for(int i = first ; i < k ; i++)
        {
            if(check(s.charAt(i)))
            {
                count++;
            }
        }

        numberOfVowels = count;

        while(last != (length - 1))
        {
            if(check(s.charAt(first)))
            {
                count--;
            }

            first++;
            last++;

            if(check(s.charAt(last)))
            {
                count++;
            }

            if(count > numberOfVowels)
            {
                numberOfVowels = count;
            }
        }

        return numberOfVowels;
    }

    public boolean check(char c)
    {
        switch(c)
        {
            case 'a': return true;
        
            case 'e': return true;

            case 'i': return true;

            case 'o': return true;

            case 'u': return true;

            default: return false;
        }
    }

}