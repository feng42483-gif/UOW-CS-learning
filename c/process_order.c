#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

//if的第一种格式
//int main()
//{
//	double temperature;
//	printf("请输入温度:");
//	scanf("%lf",&temperature);
//	if (temperature > 38.5)
//	{
//		printf("发烧了");
//	}
//	else
//	{
//		printf("没发烧");
//	}
//	return 0;
//
//}



//int main()
//{
//	int blood = 200;
//	int atk = 80;
//	int restore = 100;
//	blood = blood - atk + restore;
//	if (blood > 200)
//	{
//		blood = 200;
//	}
//	printf("%d\n", blood);
//	return 0;
//}



//第二种if格式
//int main()
//{
//	int love;
//	printf("好感度:");
//	scanf("%d",&love);
//	if (love >= 60)
//	{
//		printf("去表白");
//	}
//	else
//	{
//		printf("不去表白");
//	}
//	return 0;
//}



//int main()
//{
//	int rowA = 5;
//	int numberA = 6;
//	int rowB = 6;
//	int numberB = 7;
//	if (rowA == rowB && numberA - numberB == 1 || numberA - numberB == -1)
//	{
//		printf("我会很开心的开电影");
//	}
//	else
//	{
//		printf("我不会很开心");
//
//	}
//	return 0;
//
//}



//if的第三种条件判断
//int main()
//{
//    int card;
//
//    printf("请输入要充值的金额：");
//    scanf("%d", &card);
//
//    if (card >= 1 && card <= 99)
//    {
//        printf("VIP1");
//    }
//    else if (card >= 100 && card <= 499)
//    {
//        printf("VIP2");
//    }
//    else if (card >= 500 && card <= 999)
//    {
//        printf("VIP3");
//    }
//    else if (card >= 1000 && card <= 1999)
//    {
//        printf("VIP4");
//    }
//    else if (card >= 2000 && card <= 5000)
//    {
//        printf("VIP5");
//    }
//    else
//    {
//        printf("不是会员");
//    }
//
//    return 0;
//}


//int main()
//{
//	int score;
//	printf("请输入考试成绩");
//	scanf("%d", &score);
//	if (score >= 95 && score <= 100)
//	{
//		printf("奖励一辆自行车");
//	}
//	else if(score >= 90 && score <= 94)
//	{
//		printf("奖励游乐场玩一天");
//	}
//	else if (score >= 80 && score <= 89)
//	{
//		printf("奖励变形金刚一个");
//	}
//	else
//	{
//		printf("揍一顿");
//	}
//	return 0;
//}



int main()
{
	int week;
	printf("请输入星期几:");
	scanf("%d",&week);
	switch (week)
	{
	case 1:
		printf("使用初音未来抱枕");
		break;
	case 2:
		printf("使用雷姆抱枕");
		break;
	case 3:
		printf("使用安柏抱枕");
		break;
	case 4 :
		printf("使用芭芭拉抱枕");
		break;
	case 5:
		printf("使用可利抱枕");
		break;
	case 6:
		printf("使用蒂法抱枕");
		break;
	case 7:
		printf("使用丽莎抱枕");
		break;
	default:
		printf("没有此抱枕");
		break;




	}




}