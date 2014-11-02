import java.util.*; 
import java.io.*;

class ArithGeo {  
  String ArithGeo(int[] arr) { 
  
    int aritmethic = arr[1] - arr[0];    
    int geometric = arr[1] / arr[0];
    
    boolean arith = true;    
    boolean geo = true;
    
    for (int i = 2; i<arr.length; i++) {
      
      if (aritmethic != (arr[i]-arr[i-1])) 
          arith = false;
      if (geometric != (arr[i]/arr[i-1]))
          geo = false;
           
    }
    
   
  if(arith === true)
    return "arithmetic";    
  else if(geo === true)
    return "geometric";
     
   return "-1";
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner  s = new Scanner(System.in);
    ArithGeo c = new ArithGeo();
    System.out.print(c.ArithGeo(new int[] {2, 6, 18, 54} )); 
  }   
  
}
