//#define _CRT_SECURE_NO_WARNINGS
//#include<stdio.h>
//#include<math.h>
//#include<time.h>
//#include<stdlib.h>

//1.利用索引遍历二维数组
//int main()
//{
//	int arr[3][5] =
//	{
//		{1,2,3,4,5},
//		{11,22,33,44,55},
//		{111,222,333,444,555}
//	};
//	for (int i = 0; i < 3; i++)
//	{
//		for (int j = 0; j < 5; j++)
//		{
//			printf("%d ", arr[i][j]);
//		}
//
//		printf("\n");
//
//	}
//
//
//}

//2.
//int main()
//{
//	int arr1[3] = { 1,2,3 };
//	int arr2[5] = { 1,2,3,4,5 };
//	int arr3[9] = { 1,2,3,4,5,6,7,8,9 };
//
//	int len1 = sizeof(arr1) / sizeof(int);
//	int len2 = sizeof(arr2) / sizeof(int);
//	int len3 = sizeof(arr3) / sizeof(int);
//
//	int lenARR[3] = { len1,len2,len3 };
//
//	int* arr[3] = { arr1,arr2,arr3 };
//
//
//	for (int i = 0; i < 3; i++)
//	{
//
//		for (int j = 0; j < lenARR[i]; j++)
//		{
//			printf("%d ", arr[i][j]);
//		}
//		printf("\n");
//	}
//}

//利用指针遍历二维数组

//int main()
//{
//	int arr[3][5] =
//	{
//		{ 1, 2, 3, 4, 5 },
//	{11,22,33,44,55},
//	{111,222,333,444,555}
//	};
//
//	int(*p)[5] = arr;
//		for (int i = 0; i < 3; i++)
//		{
//			for (int j = 0; j < 5; j++)
//			{
//				printf("%d ", *(*p + j));
//			}
//			printf("\n");
//			p++;
//		}
//
//
//
//}



//int main()
//{
//	int arr1[5] = { 1,2,3,4,5 };
//	int arr2[5] = { 6,7,8,9,10 };
//	int* arr[2] = { arr1,arr2 };
//	int** p = arr;
//	for (int i = 0; i < 2; i++)
//	{
//		for (int j = 0; j < 5; j++)
//		{
//			printf("%d ", *(*p + j));
//		}
//		printf("\n");
//		p++;
//	}
//}