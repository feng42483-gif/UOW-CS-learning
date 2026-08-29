#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
int add(int num1, int num2);
int subtract(int num1, int num2);
int mutiply(int num1, int num2);
int divide(int num1, int num2);
int main()
{
	int (*arr[4])(int, int) = { add,subtract,mutiply,divide };
	printf("请录入两个数字计算\n");
	int num1, num2;
	scanf("%d%d", &num1, &num2);
	printf("%d\n", num1);
	printf("%d\n", num2);

	int choose;
	printf("请录入一个数字表示要进行的计算\n");
	scanf("%d", &choose);
	
	int res = (arr[choose - 1])(num1, num2);
	printf("%d\n", res);


	return 0;
}

int add(int num1, int num2)
{
	return num1 + num2;
}
int subtract(int num1, int num2)
{
	return num1 - num2;
}
int mutiply(int num1, int num2)
{
	return num1 * num2;
}
int divide(int num1, int num2)
{
	return num1 / num2;
}
