class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
        {
            return false;
        }

        String value = Integer.toString(x);
        String reversed = "";

        for(int i=value.length()-1 ; i>=0 ; i--)
        {
            reversed += Character.toString(value.charAt(i));
        }

        return value.equals(reversed);
    }
}