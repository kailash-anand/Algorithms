class Solution {
    public int mySqrt(int x) {
        double result = 0.0;
        
        double z = x;
        double precision = 1e-5;
        while (Math.abs(z - x / z) > precision) {
            z = (z + x / z) / 2.0;
        }
        result = z;

        return (int)Math.floor(result);
    }
}