#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>

//int main()
//{
	//int arr1[] = { 1,2,3,4,5 };
	////arr1[4] = 10;
	////int sum1 = arr1[0];
	////int sum2 = arr1[2];
	////int sum3 = arr1[4];
	////int sum = sum1 + sum2 + sum3;
	////printf("%d\n", sum);



	//for (int i = 0; i < 5; i++)
	//{
	//	printf("%d\n", arr1[i]);
	
	//int arr1[] = { 1,2,3,4,5 };
	//printf("%p\n", &arr1);
	//printf("%p\n", &arr1[0]);
	//printf("%p\n", &arr1[1]);
	//printf("%p\n", &arr1[2]);
	//
	//
//}




//int main()
//{
//	int arr[] = { 33,5,22,44,55 };
//	int max = arr[0];
//	int len = sizeof(arr) / sizeof(int);
//	for (int i = 0; i < len; i++)
//	{
//		if (arr[i] > max)
//		{
//			max = arr[i];
//		}
//	}
//	printf("%d\n",max);
//}

//int main()
//{
//	int arr[10] = { 0 };
//	int len = sizeof(arr) / sizeof(int);
//	int sum = 0; // 1. 将 sum 定义在循环外部，并初始化为 0
//
//	srand(time(NULL));
//
//	for (int i = 0; i < len; i++)
//	{
//		arr[i] = rand() % 100 + 1; // 2. 生成 1~100 的随机数赋值给数组
//		sum = sum + arr[i];        // 3. 累加到 sum 中
//	}
//
//	printf("%d\n", sum); // 正常输出累加和
//	return 0;
//}



//int main()
//{
//	int arr[5] = { 0 };
//	int len = sizeof(arr) / sizeof(int);
//	for (int i = 0; i < len; i++)
//	{
//		printf("请录入第%d个元素\n", i + 1);
//		scanf("%d", &arr[i]);
//
//		printfarr(arr, len);
//
//		int i = 0;
//		int j = len - 1;
//		while (i < j)
//		{
//			int temp = arr[i];
//			arr[i] + arr[j];
//			arr[j] = temp;
//
//			i++;
//			j++;
//		}
//
//		printfarr(arr, len);
//	}
//	return 0;
//}
//
//void printarr(int arr[], int len)
//{
//	for (int i = 0; i < len; i++)
//	{
//		printf("%d\n", arr[i]);
//	}
//}




//




//查找数组
//基本查找

//int order(int arr[], int len, int num);
//
//int main()
//{
//	int arr[] = { 11, 22, 33, 44, 55 };
//	int len = sizeof(arr) / sizeof(int);
//	int num;
//
//	printf("请输入要查找的数字：");
//	scanf("%d", &num);
//
//	int index = order(arr, len, num);
//
//	printf("%d\n", index);
//
//	return 0;
//}
//
//int order(int arr[], int len, int num)
//{
//	for (int i = 0; i < len; i++)
//	{
//		if (arr[i] == num)
//		{
//			return i;
//		}
//	}
//
//	return -1;
//}


//二分查找（数组中的数据必须有序）
//int binarySearch(int arr[], int len, int num);
//int main()
//{
//	int arr[] = { 7,23,79,81,103,127,131,147 };
//	int len = sizeof(arr) / sizeof(int);
//	int num = 131;
//	int index = binarySearch(arr, len, num);
//	printf("%d\n", index);
//	return 0;
//}
//
//int binarySearch(int arr[],int len,int num)
//{
//	int min = 0;
//	int max = len - 1;
//
//	while (min <= max)
//	{
//		int mid = (min + max) / 2;
//		if (arr[mid] > num)
//		{
//			min = mid + 1;
//		}
//		else if (arr[mid] < num)
//		{
//			max = mid - 1;
//		}
//		else
//		{
//			return mid;
//		}
//	}
//	return -1;
//}




//int binarySearch(int arr[], int len, int num);
//
//int main() {
//	int arr[] = { 7, 23, 79, 81, 103, 127, 131, 147 };
//	int len = sizeof(arr) / sizeof(int);
//	int num = 131;
//	int index = binarySearch(arr, len, num);
//	printf("%d\n", index);
//	return 0;
//}
//
//int binarySearch(int arr[], int len, int num) {
//	int min = 0;
//	int max = len - 1;
//
//	while (min <= max) {
//		int mid = min + (max - min) / 2; // 防止数值溢出
//
//		if (arr[mid] > num) {
//			max = mid - 1;
//		}
//		else if (arr[mid] < num) {
//			min = mid + 1;
//		}
//		else {
//			return mid;
//		}
//	}
//	return -1;
//}

//冒泡排序
//int main()
//{
//	int arr[] = { 3,5,1,2,4 };
//	int len = sizeof(arr) / sizeof(int);
//
//
//	for (int i = 0; i < len - 1; i++)
//	{
//		for (int j = 0; j < len - 1 - i; j++)
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				int temp = arr[j];
//				arr[j] = arr[j + 1];
//				arr[j + 1] = temp;
//			}
//		}
//	}
//	
//
//	for (int i = 0; i < len; i++)
//	{
//		printf("%d\n", arr[i]);
//	}
//
//	return 0;
//}
//first
	//for (int j = 0; j < len-1; j++)
	//{
	//	if (arr[j] > arr[j + 1])
	//	{
	//		int temp = arr[j];
	//		arr[j] = arr[j + 1];
	//		arr[j + 1] = temp;
	//	}
	//}

	////second
	//for (int i = 0; i < len - 1 - 1; i++)
	//{
	//	if (arr[i] > arr[i + 1])
	//	{
	//		int temp = arr[i];
	//		arr[i] = arr[i + 1];
	//		arr[i + 1] = temp;
	//	}
	//}
	////third
	//for (int i = 0; i < len - 1 - 2; i++)
	//{
	//	if (arr[i] > arr[i + 1])
	//	{
	//		int temp = arr[i];
	//		arr[i] = arr[i + 1];
	//		arr[i + 1] = temp;
	//	}
	//}
	////forth
	//for (int i = 0; i < len - 1 - 4; i++)
	//{
	//	if (arr[i] > arr[i + 1])
	//	{
	//		int temp = arr[i];
	//		arr[i] = arr[i + 1];
	//		arr[i + 1] = temp;
	//	}
	//}
//选择排序


int main()
{
	int arr[] = { 3,5,1,2,4 };
	int len = sizeof(arr) / sizeof(int);

	for (int i = 0; i < len - 1; i++)
	{
		for (int j = i + 1; j < len; j++)
		{
			if (arr[i] > arr[j])
			{
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}

	for (int i = 0; i < len; i++)
	{
		printf("%d\n", arr[i]);
	}

}