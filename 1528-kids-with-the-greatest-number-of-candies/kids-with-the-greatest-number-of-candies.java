class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = maxCandies(candies);
        List<Boolean> result = new LinkedList();

        for(int i = 0; i < candies.length; i++)
        {
            if(candies[i] + extraCandies >= max)
            {
                result.add(true);
            }
            else
            {
                result.add(false);
            }
        }

        return result;
    }

    public int maxCandies(int[] candies)
    {
        int max = candies[0];
        for(int i = 1; i < candies.length; i++)
        {
            if(candies[i] > max)
            {
                max = candies[i];
            }
        }
        return max;
    }
}