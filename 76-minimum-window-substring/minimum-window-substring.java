import java.util.*;

class Solution 
{
    public String minWindow(String s, String t) 
    {
        if (s.length() == 0 || t.length() == 0) return "";

        Map<Character, Integer> targetFreq = new HashMap<>();
        for (char c : t.toCharArray()) 
        {
            targetFreq.put(c, targetFreq.getOrDefault(c, 0) + 1);
        }

        int required = targetFreq.size();
        int formed = 0;
        Map<Character, Integer> windowFreq = new HashMap<>();

        int l = 0, r = 0;
        int[] ans = {-1, 0, 0};

        while (r < s.length()) 
        {
            char c = s.charAt(r);
            windowFreq.put(c, windowFreq.getOrDefault(c, 0) + 1);

            if (targetFreq.containsKey(c) && windowFreq.get(c).intValue() == targetFreq.get(c).intValue()) 
            {
                formed++;
            }

            while (formed == required) 
            {
                c = s.charAt(l);

                if (ans[0] == -1 || r - l + 1 < ans[0]) 
                {
                    ans[0] = r - l + 1;
                    ans[1] = l;
                    ans[2] = r;
                }

                windowFreq.put(c, windowFreq.get(c) - 1);
                if (targetFreq.containsKey(c) && windowFreq.get(c).intValue() < targetFreq.get(c).intValue()) 
                {
                    formed--;
                }
                l++;
            }

            r++;
        }

        return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }
}