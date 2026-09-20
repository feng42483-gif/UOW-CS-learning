#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#define N 3

void   multiplyMatrices(int A[N][N], int B[N][N], int C[N][N])
{
	for (int i = 0; i < N; i++)    //(n+1)次执行次数
	{
		for (int j = 0; j < N; j++)   //n(n+1)次执行次数
		{
			 C[i][j];               // n**2次执行次数
			for (int k = 0; k < N; k++)   //nn(n+1)次执行次数
			{
				C[i][j] += A[i][k] * B[k][j]; //n**3次执行次数
			}
		}
	}

}

//算法总频度 T(n) = (n+1) + (n^2+n) + n^2 + (n^3+n^2) + n^3 = 2n^3 + 3n^2 + 2n + 1
//\text{ 时间复杂度 } T(n) = O(n ^ 3)

void printMatrix(int matrix[N][N]) {
for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
        printf("%4d ", matrix[i][j]);
    }
    printf("\n");
}
}


int main()
{
	int A[N][N] = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}
	};

	int B[N][N] = {
		{9, 8, 7},
		{6, 5, 4},
		{3, 2, 1}
	};


	int C[N][N];
    multiplyMatrices(A, B, C);

	printf("矩阵 A:\n");
	prrintMatrix(A);

	printf("\n矩阵 B:\n");
	printMatrix(B);

	printf("\n矩阵乘积 C (A * B):\n");
	printMatrix(C);

	return 0;
}




//// 矩阵乘法函数：实现 C = A * B
//void multiplyMatrices(int A[N][N], int B[N][N], int C[N][N]) {
//    // 1. 最外层：控制结果矩阵 C 的行 (i)
//    for (int i = 0; i < N; i++) {
//        // 2. 中间层：控制结果矩阵 C 的列 (j)
//        for (int j = 0; j < N; j++) {
//            // 清零当前位置，准备累加
//            C[i][j] = 0;
//
//            // 3. 最内层：计算 A 的第 i 行与 B 的第 j 列的点积累加 (k)
//            for (int k = 0; k < N; k++) {
//                C[i][j] += A[i][k] * B[k][j];
//            }
//        }
//    }
//}
//
//// 打印矩阵的辅助函数
//void printMatrix(int matrix[N][N]) {
//    for (int i = 0; i < N; i++) {
//        for (int j = 0; j < N; j++) {
//            printf("%4d ", matrix[i][j]);
//        }
//        printf("\n");
//    }
//}
//
//int main() {
//    // 实例化两个 3x3 矩阵 A 和 B
//    int A[N][N] = {
//        {1, 2, 3},
//        {4, 5, 6},
//        {7, 8, 9}
//    };
//
//    int B[N][N] = {
//        {9, 8, 7},
//        {6, 5, 4},
//        {3, 2, 1}
//    };
//
//    // 声明用于存放计算结果的矩阵 C
//    int C[N][N];
//
//    // 调用矩阵乘法函数
//    multiplyMatrices(A, B, C);
//
//    // 输出结果
//    printf("矩阵 A:\n");
//    printMatrix(A);
//
//    printf("\n矩阵 B:\n");
//    printMatrix(B);
//
//    printf("\n矩阵乘积 C (A * B):\n");
//    printMatrix(C);
//
//    return 0;
//}