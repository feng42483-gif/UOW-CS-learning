#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>


//int main()
//{
//	int a = 10;
//	int* p = &a;
//	printf("%d\n", *p);
//	*p = 200;
//	printf("%d\n", *p);
//}
//void swap(int* num1, int* num2);
//
//int main()
//{
//	int a = 10;
//	int b = 20;
//	int temp;
//	
//	/*temp = 10;
//	a = b;
//	b = temp;
//	printf("%d\n", a);
//	printf("%d\n", b);*/
//
//	printf("%d,%d\n", a, b);
//	swap(&a, &b);
//	printf("%d,%d", a, b);
//
//	return 0;
//
//}
//
//void swap(int* num1, int* num2)
//{
//	int temp = *num1;
//	*num1 = *num2;
//	*num2 = temp;
//}

//void change(int* p)
//{
//    *p = 100;
//}
//
//int main()
//{
//    int a = 10;
//
//    change(&a);
//
//    printf("%d", a);
//}

//void getMaxAndMin(int arr[], int len, int* max, int* min);
//int main()
//{
//	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };
//	int len = sizeof(arr) / sizeof(int);
//	int max = arr[0];
//	int min = arr[0];
//	getMaxAndMin(arr, len, &max, &min);
//	printf("最大值为%d\n", max);
//	printf("最小值为%d\n", min);
//
//
//
//
//	return 0;
//
//
//}
//
//
//void getMaxAndMin(int arr[], int len, int* max, int* min)
//{
//	*max = arr[0];
//	for (int i = 1; i < len; i++)
//	{
//		if (arr[i]>*max)
//		{
//			*max = arr[i];
//		}
//	}
//	*min = arr[0];
//	for ( int i = 1; i < len;  i++)
//	{
//		if (arr[i]<*min)
//		{
//			*min = arr[i];
//		}
//	}
//
//}
int getMaxAndMi(int num1, int num2, int* res);
int main()
{
	int a = 10;
	int b = 3;
	int res = 0;
	int flag = getMaxAndMi(a, b, &res);
	if (!flag)
	{
		printf("%d\n", res);
	}
}





int  getMaxAndMi(int num1, int num2, int* res)
{
	if (res == 0)
	{
		return 1;
	}
	*res = num1 % num2;
	return 0;
}