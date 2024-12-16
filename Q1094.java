package Algorithm;

import java.util.*;

public class Q1094
{
    public static void main(String[] args)
    {   
        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter X cm : ");
        int xBar = s.nextInt();
        
        int originBar = 64;
        int count = 1;
        int mergeBar = 0;
        while (true) 
        {
            if(originBar > xBar)
            {
                originBar = originBar/2;
                mergeBar = originBar;
            }
            else if(originBar == xBar)
            {
                break;
            }
            else
            {
                mergeBar += originBar;
                count++;
                if(mergeBar > xBar)
                {
                    mergeBar -= originBar;
                    originBar = originBar / 2;
                    count--;
                }
                else if(mergeBar == xBar)
                {
                    break;
                }
                else
                {
                    originBar = originBar / 2;
                }
            }
        }
        System.out.println(count);
    }
}