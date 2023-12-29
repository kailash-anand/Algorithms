class Solution {
    public int compress(char[] chars) {
        String s = "";
        char prev = chars[0];
        int length = 1;
        s += Character.toString(prev);

        for(int i=1 ; i<chars.length ; i++)
        {
            if(chars[i] == prev)
            {
                length++;
            }
            else
            {
                if(length == 1)
                {
                    s += Character.toString(chars[i]);
                }
                else
                {
                    s += length + Character.toString(chars[i]);
                }
                length = 1;
            }
            prev = chars[i];
        }
        if(length > 1)
        {
            s += length + "";
        }
        

        for(int i=0 ; i<s.length() ; i++)
        {
            chars[i] = s.charAt(i);
        }

        return s.length();
    }
}