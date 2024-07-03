class Solution {
    public int islandPerimeter(int[][] grid) 
    {
        int perimeter = 0;

        for(int i = 0; i < grid.length; i++)
        {
            for(int j = 0; j < grid[i].length; j++)
            {
                if(grid[i][j] == 1)
                {
                    try
                    {
                        if(grid[i-1][j] == 0)
                        {
                            perimeter++;
                        }
                    }
                    catch(IndexOutOfBoundsException e)
                    {
                        perimeter++;
                    }

                    try
                    {
                        if(grid[i+1][j] == 0)
                        {
                            perimeter++;
                        }
                    }
                    catch(IndexOutOfBoundsException e)
                    {
                        perimeter++; 
                    }

                    try
                    {
                        if(grid[i][j-1] == 0)
                        {
                            perimeter++;
                        }
                    }
                    catch(IndexOutOfBoundsException e)
                    {
                        perimeter++; 
                    }


                    try
                    {
                        if(grid[i][j+1] == 0)
                        {
                            perimeter++;
                        }
                    }
                    catch(IndexOutOfBoundsException e)
                    {
                        perimeter++;
                    }    
                }
            }
        }

        return perimeter;
    }
}