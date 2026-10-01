#define _CRT_SECURE_NO_WARNINGS
#define LIST_INIT_SIZE 100
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

typedef int ElemType;
typedef struct {
	ElemType elem[LIST_INIT_SIZE];
	int length;
}SqList;


int main(void)
{
	SqList L;

	L.length = 0;
	L.elem[0] = 10;
	L.elem[1] = 20;
	L.elem[2] = 30;

	L.length = 3;

	for (int  i = 0; i < L.length; i++)
	{
		printf("%d\n", L.elem[i]);
	}
	return 0;
}