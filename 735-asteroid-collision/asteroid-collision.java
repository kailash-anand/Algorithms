class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> collider = new Stack<Integer>();
        int currentAsteroid = 0;

        for(int i = 0 ; i < asteroids.length ; i++)
        {
            if(collider.isEmpty())
            {
                collider.push(asteroids[i]);
                continue;
            }

            if(isOppositeDirection(collider.peek(),asteroids[i]))
            {
                while(Math.abs(collider.peek()) < Math.abs(asteroids[i]))
                {
                    collider.pop();

                    if(collider.isEmpty())
                    {
                        break;
                    }

                    if(!isOppositeDirection(collider.peek(),asteroids[i]))
                    {
                        break;
                    }
                }

                if(collider.isEmpty())
                {
                    collider.push(asteroids[i]);
                    continue;
                }

                if(isOppositeDirection(collider.peek(),asteroids[i]))
                {
                    if(Math.abs(collider.peek()) == Math.abs(asteroids[i]))
                    {
                        collider.pop();
                        continue;
                    }

                    if(Math.abs(collider.peek()) > Math.abs(asteroids[i]))
                    {
                        continue;
                    }
                }
            }

            collider.push(asteroids[i]);
        }

        Integer[] result = collider.toArray(new Integer[collider.size()]);
        int[] answer = new int[collider.size()];

        for(int i=0 ; i<answer.length ; i++)
        {
            answer[i] = Integer.parseInt(result[i].toString());
        }

        return answer;
    }

    public boolean isOppositeDirection(int asteroidOne, int asteroidTwo)
    {
        if(asteroidOne > 0 && asteroidTwo < 0)
        {
            return true;
        }

        return false;
    }
}