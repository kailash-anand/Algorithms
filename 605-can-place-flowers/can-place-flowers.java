class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int plantingSpaces = 0;//The number of spaces available

        //Iterates through the array to find the number of available spaces
        for(int i = 0; i < flowerbed.length; i++)
        {
            /*
            If there is a flower planted, skip the adjacent place.
            Else check if the next spot is planted. If yes, skip
            Else increment the plantingSpaces and skip th adjacent spot.
            */
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

        //Checks if the plantingSpaces are equal to or greater than n
        if(plantingSpaces >= n)
        {
            return true;
        }

        return false;
    }
}