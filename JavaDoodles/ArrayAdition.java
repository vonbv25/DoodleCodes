import java.util.*; 
import java.io.*;

class ArrayAdition {  
  String ArrayAdditionI(int[] arr) { 
    
    int max = 0;
    int sum = 0;
    for (int i = 0; i<arr.length(); i++) {
     if (max < arr[i])
       max = arr[i];      
    }
    
    for(int i = 0; i< arr.length(); i++) {
     if (arr[i]!= max)
      sum = sum + arr[i];
      
    }
    
    if (sum != max) {
      return "false";
    }
    
    
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return "true";
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    ArrayAdition c = new ArrayAdition();
    System.out.print(c.ArrayAdditionI(s.nextLine())); 
  }   
  
}








  
