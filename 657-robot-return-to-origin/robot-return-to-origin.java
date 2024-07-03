class Solution {
    public boolean judgeCircle(String moves) 
    {
        int horizontalEquilibrium = 0;
        int verticalEquilibrium = 0;

        for(int i = 0; i < moves.length(); i++)
        {
            char current = moves.charAt(i);

            if(current == 'U')
            {
                verticalEquilibrium++;
            }

            if(current == 'D')
            {
                verticalEquilibrium--;
            }

            if(current == 'R')
            {
                horizontalEquilibrium++;
            }

            if(current == 'L')
            {
                horizontalEquilibrium--;
            }
        }

        if(horizontalEquilibrium == 0 && verticalEquilibrium == 0)
        {
            return true;
        }
        
        return false;
    }
}