import java.util.*; 
import java.io.*;

class LetterCapitalize {  
  String LetterCapitalize(String str) { 
  
    String[] _split= str.split(" ");
    String space = " ";
    String _result  = "";
    for(String _str: _split ) {
       if (_str.charAt(0) >='a' && _str.charAt(0) <='z')
            _result += ((char) (_str.charAt(0) -32));
      else
        _result+= _str.charAt(0);
      for(int i = 1; i< _str.length();i++) {
        _result+=_str.charAt(i);
      }
      _result+=space;
      
    }
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return _result;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    LetterCapitalize c = new LetterCapitalize();
    System.out.print(c.LetterCapitalize(s.nextLine())); 
  }   
  
}








  
