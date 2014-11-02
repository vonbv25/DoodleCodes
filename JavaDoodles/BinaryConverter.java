import java.util.*; 
import java.io.*;

class BinaryConverter {  
  int BinaryConverter(String str) { 
  
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
    int sum = 0;
    for(int x=0; x<str.length(); x++)
    {
      if(str.charAt(x) == '1')
      {
        sum += Math.pow(2,(str.length()-1) - x);
      }
    } 
    
    return sum;
       
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    BinaryConverter c = new BinaryConverter();
    System.out.print(c.BinaryConverter(s.nextLine())); 
  }   
  
}           

