#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>


//struct Student
//{
//	char name[100];
//	int age;
//};
//int main()
//{
//	struct Student stu1 = { "zhangsan",23 };
//	struct Student stu2 = { "lisi",18 };
//	struct Student stu3 = { "wangwu",15 };
//	struct Student  stuArr[3] = { stu1,stu2,stu3 };
//	for (int  i = 0; i < 3; i++)
//	{
//		struct Student temp = stuArr[i];
//		printf("%s,%d\n", temp.name, temp.age);
//
//	}
//
//	return 0;
//
//
//}

//typedef struct game
//{
//	char name[100];
//	int attack;
//	int defense;
//	int blood;
//}M;
//
//int main()
//{
//	M taro = { "泰罗",100,90,500 };
//	M rem = { "雷欧",90,80,450 };
//	M eddie = { "艾迪",120,70,600 };
//
//	M arr[3] = { taro,rem,eddie };
//	for (int i = 0; i < 3; i++)
//	{
//		M temp = arr[i];
//		printf("%s.%d,%d,%d\n", temp.name, temp.attack, temp.defense, temp.blood);
//		
//	}
//	
//	return 0;
//}


//typedef struct student
//{
//	char name[100];
//	int age;
//}S;
//void method(S* st);
//
//int main()
//{
//
//	S stu;
//	strcpy(stu.name, "aaa");
//	stu.age = 0;
//	printf("%s,%d\n", stu.name, stu.age);
//	method(&stu);
//	printf("%s,%d\n", stu.name, stu.age);
//
//}
//
//void method(S* st)
//{
//	printf("%s,%d\n", (*st).name, (*st).age);
//	printf("请输入修改的学生名字：");
//	scanf("%s", (*st).name);
//	printf("请输入修改的学生名字：");
//	scanf("%d", &((*st).age));
//	printf("%s,%d\n", (*st).name, (*st).age);
//}


struct spot
{
	char name[100];
	int count;
};

int main()
{

	struct spot arr[4] = { {"A",0},{"B",0},{"C",0},{"D",0} };

	srand(time(NULL));
	for (int i = 0; i < 80; i++)
	{
		int choose = rand() % 4; 
		arr[choose].count++;
	}

	int max = arr[0].count;
	for (int i = 1; i < 4; i++)
	{
		struct spot temp = arr[i];
		if (temp.count>max)
		{
			max = temp.count;
		}
	}



	for (int i = 0; i < 4; i++)
	{
		struct spot temp = arr[i];
		if (temp.count == max)
		{
			printf("%s %d\n", temp.name, temp.count);
			break;
		}
	}



	for (int i = 0; i < 4; i++)
	{
		struct spot temp = arr[i];
		printf("%s %d\n", temp.name, temp.count);
	}

}