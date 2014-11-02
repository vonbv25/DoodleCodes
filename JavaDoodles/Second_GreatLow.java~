import java.util.*; 
import java.io.*;

class Second_GreatLow {  
  String SecondGreatLow(int[] arr) { 

     
    for (int i =0; i< arr.length; i++) {
      for (int j = 0; j< arr.length-1; j++) {
        if (arr[j] > arr[j+1]) {
            int temp = arr[j+1];
            arr[j+1] = arr[j];
            arr[j] = temp;
        }
        
      }
      
    }
    
    
    
    // code goes here   
    /* Note: In Java the return type of a function and the 
       parameter types being passed are defined, so this return 
       call must match the return type of the function.
       You are free to modify the return type. */
       
    return  ""+arr[1]+ " " + arr[arr.length-2] +"";
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    Second_GreatLow c = new Second_GreatLow();
    System.out.print(c.SecondGreatLow(new int[] {1,2,3,100})); 
  }   
  
}








  
