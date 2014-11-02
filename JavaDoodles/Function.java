import java.util.*; 
import java.io.*;

class Function {  
  String LongestWord(String sen) { 
  
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
	String[] str_split = sen.split("[^a-zA-Z0-9]+");
	int max = 0;
	String _str = "";
	for (String str: str_split) {		
		if (max < str.length()) {
		max = str.length();
		_str= str;
		}
	
	}
       
    return _str;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    Function c = new Function();
    System.out.print(c.LongestWord(s.nextLine())); 
  }   
  
}
 
