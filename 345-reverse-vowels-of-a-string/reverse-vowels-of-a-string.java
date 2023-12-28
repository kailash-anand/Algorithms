class Solution {
    public String reverseVowels(String s) 
    {
        int length = s.length();
        int count = 0;
        char[] c = new char[length];
        int first = 0;
        int last = length-1;
        String reversed = "";

        while(first < length)
        {
            if(!check(s.charAt(first)))
            {
                c[count++] = s.charAt(first);
                first++;
            }
            else
            {
                while(!check(s.charAt(last)))
                {
                    last--;
                }
                c[count++] = s.charAt(last);
                last--;
                first++;
            }
        }

        return String.valueOf(c);
    }

    public boolean check(char c)
    {
        switch(Character.toLowerCase(c))
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