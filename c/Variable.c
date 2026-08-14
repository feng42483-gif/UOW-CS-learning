//#include <stdio.h>

//int main()
//{
	//数据类型：short,int,long,long long

	//short 短整型 windwows 2字节
	//short range(-32768 - 32768)
	//int range  windows 4字节  (-2147483648 - 2147483647)
	//long c = 1000L;
	//printf("%ld\n", c);
    //long long 超长整型 windows 8字节（19位数）
	//long long d = 100000LL;
	//printf("%lld", d);

	//利用sizer 测量每一种数据类型占用多少字节
	//printf("%zu\n", sizeof(short));
	//printf("%zu\n", sizeof(c));

	//signed有符号整数，正数，负数
	//unsigned 无符号整数 正数

	//signed int e = -100;
	//printf("%d", e);

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
	int main()
	{
		double length;
		double width;
		double height;

		printf("请输入三个小数，分别表示长宽高：");
		scanf_s("%lf %lf %lf", &length, &width, &height);

		double areaA = length * width;
		double areaB = height * width;
		double areaC = length * height;

		printf("A面的面积为：%.2f\n", areaA);
		printf("B面的面积为：%.2f\n", areaB);
		printf("C面的面积为：%.2f\n", areaC);

		double bulk = length * width * height;
		printf("长方体的体积为：%.2lf\n", bulk);


		return 0;
	}


//}