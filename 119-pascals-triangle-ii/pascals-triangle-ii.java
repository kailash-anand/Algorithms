class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> dynamicRow = new ArrayList<>();

        for(int i=0 ; i<=rowIndex ; i++)
        {
            if(i == 0 || i == 1)
            {
                dynamicRow.add(1);
                continue;
            }

            List<Integer> temp = new ArrayList<>();
            dynamicRow.forEach(element -> temp.add(element));
            dynamicRow.clear();
            dynamicRow.add(1);
            IntStream.range(0, temp.size()-1).forEach(
                    val -> dynamicRow.add(temp.get(val) + temp.get(val+1))
                );
            dynamicRow.add(1);
        }
        return dynamicRow;
    }
}