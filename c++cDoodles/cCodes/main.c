#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char firstReverse(char str) {

     char tobeReturn[strlen(str)];
     int i;
     int j = 0;
     for(i = strlen(str)-1; i> 0; i--) {

        tobeReturn[j] = str[i];
        j++;
     }


    return tobeReturn;
}

int main()
{

    char str[] = "Argument goes here";
    char *tobeReturn;
    tobeReturn= (char*) malloc(strlen(str));
    printf("%i",strlen(tobeReturn));
    return 0;
}
