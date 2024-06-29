class Solution {
    public boolean isValid(String s) 
    {
        Deque<Character> stack = new ArrayDeque<Character>();
        char current = ' ';
        
        for(int i = 0; i < s.length(); i++)
        {
            current = s.charAt(i);

            if(current == '[' || current == '{' || current == '(')
            {
                stack.addFirst(current);
            }
            else
            {
                if(stack.isEmpty() || isNotPair(current, stack.peekFirst()))
                {
                    return false;
                }
                else
                {
                    stack.removeFirst();
                }
            }
        }

        if(!stack.isEmpty())
        {
            return false;
        }

        return true;
    }

    public boolean isNotPair(char first, char second)
    {
        switch(first)
        {
            case ']':
                if(second == '[')
                {
                    return false;
                }
            break;

            case '}':
                if(second == '{')
                {
                    return false;
                }
            break;

            case ')':
                if(second == '(')
                {
                    return false;
                }
            break;
        }

        return true;
    }
}