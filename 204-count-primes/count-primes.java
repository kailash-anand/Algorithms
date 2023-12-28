class Solution 
{
    public int countPrimes(int n) 
    {
        int index =0 ;
        
        if(n == 0 || n == 1)
        { return 0; }

        boolean[] check = new boolean[n];
        
        for(int i=2 ; i<n ; i++)
        {
            if(!check[i])
            {
                index += 1;

                for(int j=i ; j<n ; j+=i)
                {
                    check[j] = true;
                }
            }
        }

        return index;
        

    }
}