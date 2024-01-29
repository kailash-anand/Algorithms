class Solution {
    public String removeStars(String s) {
        String ans = "";
        char[] string = s.toCharArray();
        Stack<Character> input = new Stack<Character>();

        for(int i=0 ; i<string.length ; i++)
        {
            if(string[i] == '*')
            {
                input.pop();
                continue;
            }

            input.push(string[i]);
        }

        ans=input.stream().map(val -> val.toString()).collect(Collectors.joining());
        return ans;
    }
}