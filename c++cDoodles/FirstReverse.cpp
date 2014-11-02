#include<iostream>
#include<stdlib>

int main( )
{
	clrscr( );
	char str[];
	cout<<"Enter a string:";
	gets(str);

	for(int l=0; str[l]!='\0';l++);		//Loop to find the length of the string

	for(int i=l-1;i>=0;i--)			//Loop to display the string backwards
		cout<<str[i];

	getch();
	return 0;
}

 

 
