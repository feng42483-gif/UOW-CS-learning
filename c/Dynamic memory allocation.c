#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

int main()
{

	 int* p =malloc(100 * sizeof(int));
	 //int* p =calloc(10 * sizeof(int));

	 for (int i = 0; i < 10; i++)
	 {
		 //*(p + i) = (i + 1) * 10;
		 p[i] = (i + 1) * 10;
	 }


	 for (int i = 0; i < 10; i++)
	 {
		 printf("%d\n", *(p + i));
	 }

	 free(p);
 
}