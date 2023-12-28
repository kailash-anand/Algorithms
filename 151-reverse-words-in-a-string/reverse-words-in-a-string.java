class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        int length = s.length();
        int last = length;
        int first = 0;
        int step = 1;
        String reversed = "";

        for(int i=length-1 ; i > 0 ; i--)
        {
            if(s.charAt(i) == ' ')
            {
                if(s.charAt(i-1) == ' ')
                {
                    step++;
                    continue; 
                }
                first = i+step;
                step = 1;
                reversed = reversed + s.substring(first,last) + " ";
                last = i;
            }

        }

        int count = 0;
        while(count < s.length() && s.charAt(count) != ' ')
        {
            count++;
        }
        reversed += s.substring(0,count);
        return reversed;
    }
}