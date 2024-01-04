class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparing(element -> element[0]));

        int endpoint = intervals[0][1];
        int minOverlaps = 0;

        for(int i = 1; i < intervals.length ; i++)
        {
            int[] currentInterval = intervals[i];

            if(currentInterval[0] < endpoint)
            {
                endpoint = Math.min(endpoint,currentInterval[1]);
                minOverlaps++;
            }
            else
            {
                endpoint = currentInterval[1];
            }
        }
        
        return minOverlaps;
    }
}