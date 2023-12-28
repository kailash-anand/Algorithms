class Solution 
{
    public void rotate(int[][] matrix) 
    {
        int row = matrix.length;
		 int column = matrix.length;
		 
		 int step = 0;
		 int check = matrix.length/2;
		 
		 int[][] duplicate = new int[row][column];
		 
		 for(int i=0 ; i<matrix.length ; i++)
		 {
			 for(int j=0 ; j<matrix[0].length ; j++)
			 {
				duplicate[i][j] = matrix[i][j];
			 }
		 }
		 		 
		 while(step<check)
		 {
			 for(int j=0+step ; j<matrix[0].length-step ; j++)
			 {
				 matrix[step][j] = duplicate[matrix.length-1-j][step];
				 matrix[matrix.length-1-step][j] = duplicate[matrix.length-1-j][matrix.length-1-step];
				 matrix[j][step] = duplicate[matrix.length-1-step][j];
				 matrix[j][matrix.length-1-step] = duplicate[step][j];
			 }
			 step++;
		 }
    }
}
    