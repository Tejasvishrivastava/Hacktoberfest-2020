import java.io.*;
import java.lang.*;
import java.util.*;
class temperature
{
    int temp;
    temperature()
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the temperature:\n ");
        temp = in.nextInt();
        if(temp!=0)
        {
         System.out.println("Value accepted \n");
        }
        try
        {
            if(temp==0)
            {
                throw new Exception("Error");
            }
        }
        catch(Exception e)
        {
            System.out.println("Temperature cannot be zero(try other value)");
        }
    }
}
public class program3b {
    public static void main(String args[])
    {
        temperature t = new temperature(); }
}