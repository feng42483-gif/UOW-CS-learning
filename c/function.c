#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
//int sum(int sum1,int sum2)
//{
//	int sum = sum1 + sum2;
//	printf("%d", sum);
//	return sum;
//}
//
//int main()
//{
//	sum(10,20);
//		return 0;
//}



//double get_circle_area(double r)
//{
//    return 3.14 * r * r;
//}
//
//int main()
//{
//    double area1 = get_circle_area(5);
//    double area2 = get_circle_area(10);
//
//    if (area1 > area2)
//    {
//        printf("第一个面积大\n");
//    }
//    else if (area1 < area2)
//    {
//        printf("第二个面积大\n");
//    }
//    else
//    {
//        printf("两个一样大\n");
//    }
//
//    return 0;
//}
//int main()
//{
	////pow幂
	//double res1 = pow(2, 3);
	//printf("%lf\n", res1);

	////sqrt()平方根
	//double res2 = sqrt(8);
	//printf("%lf\n", res2);

	////ceil()向上取整
	//double res3 = ceil(12.3);
	//printf("%lf\n", res3);

	////floor() 向下取整
	//double res4 = floor(12.7);
	//printf("%lf\n", res4);

	////abs()绝对值
	//int res5 = abs(-13);
	//printf("%d\n", res5);


	/*long long res = time(NULL);
	printf("%lld\n", res);*/

	/*srand(1);
	int num = rand();
	printf("%d\n", num);*/

	/*strand(time(NULL));
	int sum = rand() % 76 + 12;
	printf("%d\n", sum);

}*/


int main()
{
	srand(time(NULL));
	int num = rand() % 100 + 1;
	int guess;
	while (1)
	{
		printf("请输入要猜的数字；\n");
		scanf("%d", &guess);

		if (guess < num)
		{
			printf("小了\n");
		}
		else if (guess > num)
		{
			printf("大了\n");
		}
		else
		{
			printf("中了\n");
		}
	}

}