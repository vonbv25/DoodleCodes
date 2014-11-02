import java.util.*; 
import java.io.*;

class SimpleSymbols {  
 
  String SimpleSymbols(String str) { 
    
    if (str.length()<3)
        return "false";
    
    for (int i = 0; i< str.length();i++) {
     if ( ( (str.charAt(i)>='a' && str.charAt(i)<='z') 
           || (str.charAt(i)>='A' && str.charAt(i)<='Z') ) && isValid(str,i))
           return "false";
      
    }
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return "true";
    
  } 
  
  boolean isValid(String str,int index) {
    if (index==0) 
      return true;
    
    if (str.charAt(index-1)!='+' || str.charAt(index+1)!='+')
      return true;
    else
      return false;
  }

  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    SimpleSymbols c = new SimpleSymbols();
    System.out.println(c.SimpleSymbols(s.nextLine())); 
  }   
  
}








  
