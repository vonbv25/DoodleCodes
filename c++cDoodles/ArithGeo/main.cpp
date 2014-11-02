#include <iostream>
#include <string>
#include <sstream>
#include <typeinfo>
using namespace std;

string ArithGeo(int *arr, int size) {

        int arithmetic = arr[1]- arr[0];
        int geometric = arr[1]/arr[0];
        bool isArithetic = false;
        bool isGeo = false;

        for(int i = 2; i< size; i++) {
            if (arr[i]- arr[i-1]== arithmetic) {
                isArithetic = true;
                }

            else if (arr[i]/arr[i-1]== geometric) {
                isGeo = true;
                }

      }


    if (isArithetic)
        return "Arithmetic";
    else if (isGeo)
        return "Geometric";
      // code goes here
    else
        return "-1";

    }

string FirstReverse(string str) {
    string temp = "";

    for (int i = str.length()-1; i>=0; i--) {
        temp = temp + str[i];
    }

    return temp;

}

int factorial(int n) {
if (n == 0)
    return 1;
else
    return n*factorial(n-1);

return n;
}

string letterChanges(string str) {
    string _str=  "";
    string __str = "";

    for(int i = 0; i< str.length(); i++ ) {
        if (str.at(i) >= 'a' && str.at(i)<='z')
            _str += (( char)    ((((str.at(i)-'a')+1) % 26) + 'a') );
        else
            _str += str.at(i);
    }

    for (int i  = 0; i< _str.length(); i++) {
        if (((_str.at(i)=='a'|| _str.at(i)=='e')|| _str.at(i)=='i') || (_str.at(i)=='o'|| _str.at(i)=='u') )
            __str+= (( char)    ((((str.at(i)-'a')+1) % 26) + 'A') );
        else
            __str += _str.at(i);
    }

    return __str;



}

string letterCapitalize(string str) {

    string result = "";
    str = str + " ";
    int start = 0;

    for (int i = 0; i< str.length();i++) {
        if (str.at(i)==' ') {
                string token = str.substr(start,i-start);
                if (token.at(0)>='a' && token.at(0)<='z')
                    result = result + ((char) ( (token.at(0)-'a') +'A')  );
                else
                    result = result + token.at(0);

                for(int j = 1; j<token.length();j++)
                    result= result + token.at(j);

                start = i+1;
                result = result + " ";
        }
    }


    return result;
}

string longestWord(string str) {
    string clean = "";
    int start = 0;

    for (int i = 0; i< str.length(); i++) {
        if ( (( str.at(i)>='a' && str.at(i)<='z') || (str.at(i)>='A' && str.at(i)<='Z') ) || str.at(i)==' ')
        clean = clean + str.at(i);
    }
    clean = clean + " ";
    string toBecompare = "";
    for (int i =0; i< clean.length();i++) {
        if (clean.at(i)== ' ') {
            string token = clean.substr(start,i-start);
                if (token.length()> toBecompare.length()) {
                    toBecompare = token;
                }
            start= i +1;
            }
    }

    return toBecompare;
}

bool isValid(string str, int index) {
    if (index==0)
        return true;
    if (str.at(index-1)!='+' || str.at(index+1)!='+')
        return true;
    else
        return false;
}

string simpleSymbols (string str) {
    if (str.length() < 3)
        return "false";

    for (int i = 0; i< str.length();i++) {
        if ( ( (str.at(i)>='a'&& str.at(i)<='z')
            || (str.at(i)>='A' && str.at(i)<='Z') ) && isValid(str,i) )
            return "false";

    }

    return "true";



}

string timeConvert(int n ) {
    int hours = n/60;
    int mins = n%60;

    ostringstream convert;
    convert<<hours<<":"<<mins;
    string result = convert.str();

    return  result;



}

string alphabetSoup(string str) {

    for(int i = 0; i <str.length();i++) {
        for(int j = 0; j< str.length()-1;j++) {
            if(str[j]> str[j+1]) {
                char temp = str[j];
                str[j]= str[j+1];
                str[j+1]= temp;
            }
        }
    }
    return str;
}

string cipher(string str,int shifts) {

    string result = "";
    for (int i = 0; i< str.length() ;i++) {
        if (str.at(i)== ' ')
            result = result + str.at(i);
        else
            if (str.at(i)>='a' && str.at(i)<='z')
                    result = result +  ((char)((((str.at(i)-'a') + shifts) % 26)+'a') );
            else if (str.at(i)>='A' && str.at(i)<='Z')
                    result = result +  ((char)((((str.at(i)-'A') + shifts) % 26)+'A') );
            else
                result = result + str.at(i);

    }
    return result;
}




int main() {

      // keep this function call here
      /* Note: In C++ you first have to initialize an array and set
         it equal to the stdin to test your code with arrays.
         To see how to enter arrays as arguments in C++ scroll down */

        string str = "Argument goes here";
        string str2 = "coderbytes";
        string symbols = "+d+=3=+s+";
        string symbols2 = "f++d+";
        string tobeCipher  ="Ceasar cipher";
        int months[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        int time = 100;
        cout<< "1)." + FirstReverse(str)<<endl;

        int arr[] = {1,2,3,4};
        int size = (sizeof(arr)/sizeof(*arr));
        cout<<"2)." + ArithGeo(arr,size)<<endl;

        int n = 5;
        cout<<"3).";cout<<factorial(n)<<endl;

        cout<<"4)." + letterChanges(str)<<endl;
        cout<<"5)." + letterCapitalize(str)<<endl;
        cout<<"6)." + longestWord(str)<<endl;
        cout<<"7)." + simpleSymbols(symbols)<<endl;

        cout<<"8)." + timeConvert(time)<<endl;
        cout<<"9)." + alphabetSoup(str2)<<endl;
        cout<<"10)." + cipher(tobeCipher,3)<<endl;
        cout<<months[4];

        return 0;

}















