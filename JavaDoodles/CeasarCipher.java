import java.util.*; 
import java.io.*;

class CaesarCipher {  
  String CaesarCipher(String str, int num) { 
  
    String[] tokens = str.split(" ");
    String result  = "";
    for (String token: tokens) {
      
      for(int i = 0; i< token.length();i++) {
       if (token.charAt(i)>='a'&& token.charAt(i)<='z')
           result= result + ((char)((((token.charAt(i)-'a')+num)%26)+'a'));
       else if (token.charAt(i)>='A'&& token.charAt(i)<='Z')
           result= result + ((char)((((token.charAt(i)-'A')+num)%26)+'A'));
        else 
          result = result + token.charAt(i);

      }
      result = result + " ";

    }
    
    
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return result;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    CaesarCipher c = new CaesarCipher();
    System.out.print(c.CaesarCipher(s.nextLine())); 
  }   
  
}           

