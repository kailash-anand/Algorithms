class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();

        if(numRows <= 0)
        {
            return triangle;
        }

        temp.add(1);
        triangle.add(temp);
        if(numRows != 1)
        {
            temp = new ArrayList<>();
            temp.add(1);
            temp.add(1);
            triangle.add(temp);
        }
        
        for(int i=2 ; i<numRows; i++)
        {
            temp = new ArrayList<>();
            int length = triangle.get(i-1).size();
            temp.add(1);
            for(int j=1 ; j<length ; j++)
            {
                temp.add(triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j));
            }
            temp.add(1);
            triangle.add(temp);
        }
    
        return triangle;
    }
}