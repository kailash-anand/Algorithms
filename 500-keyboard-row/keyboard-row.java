class Solution {
    public String[] findWords(String[] words) 
    {
        final String FIRST = "qwertyuiopQWERTYUIOP";
        final String SECOND = "asdfghjklASDFGHJKL";
        final String THIRD = "zxcvbnmZXCVBNM";

        boolean firstSwitch = false;
        boolean secondSwitch = false;
        boolean thirdSwitch = false;

        List<String> filteredWords = new LinkedList<String>();

        for(int i = 0; i < words.length; i++)
        {
            firstSwitch = false;
            secondSwitch = false;
            thirdSwitch = false;

            for(int j = 0; j < words[i].length(); j++)
            {
                if(FIRST.contains(String.valueOf(words[i].charAt(j))))
                {
                    firstSwitch = true;
                }
                else if(SECOND.contains(String.valueOf(words[i].charAt(j))))
                {
                    secondSwitch = true;
                }
                else if(THIRD.contains(String.valueOf(words[i].charAt(j))))
                {
                    thirdSwitch = true;
                }

                if((firstSwitch && secondSwitch) || (firstSwitch && thirdSwitch) ||
                    (secondSwitch && thirdSwitch))
                {
                    break;
                }
            }

            if(!((firstSwitch && secondSwitch) || (firstSwitch && thirdSwitch) ||
                    (secondSwitch && thirdSwitch)))
            {
                filteredWords.add(words[i]);
            }
        }

        Object[] objectArray = filteredWords.toArray();
        String[] stringArray = Arrays.copyOf(objectArray, objectArray.length, String[].class);

        return stringArray;
    }
}