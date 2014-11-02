import java.util.*; 
import java.io.*;

class letterCount {  
  String LetterCountI(String str) { 
    String tobeReturn ="";
    int _count = 0;
    String[] tokens = str.split(" ");
    
    for (String token: tokens) {
       int[] _alpha= new int[26];  
      for (int i = 0; i< token.length();i++) {
          if (token.charAt(i)>='A' && token.charAt(i)<='Z')
              _alpha[token.charAt(i)-'A']++;
          else if (token.charAt(i)>='a' && token.charAt(i)<='z')
              _alpha[token.charAt(i)-'a']++;
      }
      
      int count = 0;
        
      for (int i = 0; i<_alpha.length;i++) {
        if (_alpha[i]>1) {
            count = count + 1;  
        }
      }
      if (count>_count) {
         _count = count;
        tobeReturn = token;
      } 
    
    }
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */

    if (tobeReturn=="")
	tobeReturn = "-1";
       
    return tobeReturn;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    letterCount c = new letterCount();
    System.out.print(c.LetterCountI(s.nextLine())); 
  }   
  
}








  
