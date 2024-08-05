class Solution 
{
    public int numJewelsInStones(String jewels, String stones) 
    {
        int jewelCount = 0;

        for(int i = 0; i < stones.length(); i++)
        {
            char stone = stones.charAt(i);

            if(jewels.contains(Character.toString(stone)))
            {
                jewelCount++;
            }
        }

        return jewelCount;
    }
}