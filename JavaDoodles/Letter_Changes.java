import java.util.*; 
import java.io.*;

class Letter_Changes {  
  String LetterChanges(String str) { 
  
    String _str = "";
    String __str = "";

    for(int i = 0; i< str.length();i++) {
	if (str.charAt(i)>= 'a' && str.charAt(i)<='z')
	_str +=  (char) (( ( (str.charAt(i)-'a') + 1 ) % 26) + 'a');	
	else
	_str += str.charAt(i);

             
    }

	for (int i = 0; i< _str.length();i++) {
	if(( ( ( ( (_str.charAt(i)=='a') || (_str.charAt(i)=='e') ) || (_str.charAt(i)=='i') ) || (_str.charAt(i)=='o') ) || (_str.charAt(i)=='u') ))
		__str += (char)( ( ( (str.charAt(i) -'a')+1 )%26) + 'A');
	else
	__str += _str.charAt(i);
	}  
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return __str;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    Letter_Changes c = new Letter_Changes();
    System.out.println(c.LetterChanges(s.nextLine())); 
  }   
  
}








  
