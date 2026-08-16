#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>


//int main()
//{
//	int week;
//	printf("请输入星期几:");
//	scanf("%d", &week);
//	switch (week)
//	{
//	case 1:
//		printf("使用初音未来抱枕");
//		break;
//	case 2:
//		printf("使用雷姆抱枕");
//		break;
//	case 3:
//		printf("使用安柏抱枕");
//		break;
//	case 4:
//		printf("使用芭芭拉抱枕");
//		break;
//	case 5:
//		printf("使用可利抱枕");
//		break;
//	case 6:
//		printf("使用蒂法抱枕");
//		break;
//	case 7:
//		printf("使用丽莎抱枕");
//		break;
//	default:
//		printf("没有此抱枕");
//		break;
//
//	}


//int main()
//{
//    int n;
//    scanf("%d", &n);
//
//    while (n > 1)
//    {
//        if (n % 2 != 0)
//        {
//            printf("no");
//            return 0;
//        }
//
//        n = n / 2;
//    }
//
//    printf("yes");
//
//    return 0;
//}

//int main()
//{
//	int moutain = 8844430;
//	double thickness = 0.1;
//	int times = 0;
//	while (thickness < moutain)
//	{
//		thickness *= 2;
//		times += 1;
//	}
//	printf("总共需要%d次", times);
//}



#include <math.h>

int main()
{
    int x;
    scanf("%d", &x);

    int result = (int)sqrt(x);

    printf("%d\n", result);

    return 0;
}