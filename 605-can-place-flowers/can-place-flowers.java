class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int plantingSpaces = 0;

        for(int i = 0; i < flowerbed.length; i++)
        {
            if(flowerbed[i] == 1)
            {
                i++;
                continue;
            }
            else
            {
                if(i+1 < flowerbed.length && flowerbed[i+1] == 1)
                { continue; }
                plantingSpaces++;
                i++;
                continue;
            }
        }

        if(plantingSpaces >= n)
        {
            return true;
        }

        return false;
    }
}