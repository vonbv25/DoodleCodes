#include <iostream>
using namespace std;

int ArithGeo(int arr[]) {


  int arithmetic = arr[1]- arr[0];
  int geometric = arr[1]/arr[0];




  // code goes here
  return arr[0];

}

int main() {

  // keep this function call here
  /* Note: In C++ you first have to initialize an array and set
     it equal to the stdin to test your code with arrays.
     To see how to enter arrays as arguments in C++ scroll down */

  int A[] = gets(stdin);
  cout << ArithGeo(A);
  return 0;

}

