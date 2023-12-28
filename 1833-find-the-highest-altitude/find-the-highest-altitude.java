class Solution {
    public int largestAltitude(int[] gain) {
        int length = gain.length;
        int sum = 0;
        int max = 0;
        int[] altitudes = new int[length + 1];

        altitudes[0] = 0;
        for(int i=1 ; i<altitudes.length ; i++)
        {
            sum += gain[i-1];
            altitudes[i] = sum;
            if(altitudes[i] > max)
            {
                max = altitudes[i];
            }
        }

        return max;
    }
}