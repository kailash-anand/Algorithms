import java.util.*;
public class Solution {

   public static int romanToInt(String s) {
        int num = 0;
        for(int i=0 ; i<s.length() ; i++)
        {
            switch(s.charAt(i))
        {
                case('I'): num += 1;
                break;
                
                case('V'):if(i>=1) {
                	if(s.charAt(i-1) == 'I')
                {
                	num = num + 5 - 2 ;
                	break;
                }
                }
                	num += 5;
                    break;
                
                case('X'):if(i>=1) {
                	if(s.charAt(i-1) == 'I')
                {
                	num = num + 10 - 2 ;
                	break;
                }
                }
                	num += 10;
                    break;
                
                case('L'):if(i>=1) {
                	if(s.charAt(i-1) == 'X')
                {
                	num = num + 50 - 20 ;
                	break;
                }
                }
                	num += 50;
                    break;
                
                case('C'):if(i>=1) {
                	if(s.charAt(i-1) == 'X')
                {
                	num = num + 100 - 20 ;
                	break;
                }
                }
                   	num += 100;
                    break;
                
                case('D'):if(i>=1) {
                	if(s.charAt(i-1) == 'C')
                {
                	num = num + 500 - 200 ;
                	break;
                }
                }
                   	num += 500;
                    break;
                
                case('M'):if(i>=1) {
                	if(s.charAt(i-1) == 'C')
                {
                	num = num + 1000 - 200;
                	break;
                }
                } 
                    num += 1000;
                    break;
        }   
        }
        return num;
    }

public static void main(String[] args)
{
    Scanner input = new Scanner(System.in);
    System.out.print("Enter a roman number: ");
    String s = input.nextLine();
    int s2 = romanToInt(s);
    System.out.println(s2);
}
}