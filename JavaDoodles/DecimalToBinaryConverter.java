import java.util.*; 
import java.io.*;

public class DecimalToBinaryConverter {

 String decimalToBinaryConverter (int n) {
	String result ="";
	String reverse = "";
	int div = n;
	
	while (div>0) {
		int mod = div%2;
		 div = div/2;
		result = result + "" + mod;
	}
	for (int i = result.length()-1;i>=0;i--)
		reverse = reverse + result.charAt(i);
	
    	return reverse;
  }

  public static void main(String args[]) {

   Scanner  s = new Scanner(System.in);
   DecimalToBinaryConverter c = new DecimalToBinaryConverter();
   System.out.print(c.decimalToBinaryConverter(s.nextInt())); 		

   }

}
