import java.util.*; 
import java.io.*;

class Palindrome {  
  String Palindrome(String str) { 
  
    String original = "";
    String reverse = "";
    for(int i = 0; i<str.length(); i++)
      if (str.charAt(i)!=' ')
        original = original + str.charAt(i);

      for(int i = original.length()-1; i>=0; i--)
      reverse = reverse + original.charAt(i);
      
      if (original.equals(reverse))
      return "true";
      
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return "false";
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    Palindrome c = new Function();
    System.out.print(c.Palindrome(s.nextLine())); 
  }   
  
}








  
