//#define _CRT_SECURE_NO_WARNINGS
//#include<stdio.h>
//#include<math.h>
//#include<time.h>
//#include<stdlib.h>
//#include<string.h>


typedef struct {
	float realpart;
	float imagpart;
}Complex;


void assign(Complex* A, float real, float imag) 
{
	A->realpart = real;
	A->imagpart = imag;
}

void add(Complex* C, Complex A, Complex B)
{
	C->realpart = A.realpart + B.realpart;
	C->imagpart = A.imagpart + B.imagpart;
}


void subtract(Complex* C, Complex A, Complex B) {
	C->realpart = A.realpart - B.realpart;
	C->imagpart = A.imagpart - B.imagpart;
}

// 公式：(a + bi)(c + di) = (ac - bd) + (ad + bc)i
void multiply(Complex* C, Complex A, Complex B) {
	C->realpart = A.realpart * B.realpart - A.imagpart * B.imagpart;
	C->imagpart = A.realpart * B.imagpart + A.imagpart * B.realpart;
}

void printComplex(Complex C) {
	if (C.imagpart >= 0) {
		printf("%.2f + %.2fi\n", C.realpart, C.imagpart);
	}
	else {
		printf("%.2f - %.2fi\n", C.realpart, -C.imagpart);
	}
}
int main() {
    Complex num1, num2, result;

    // 给 num1 赋值为 3 + 4i，num2 赋值为 1 - 2i
    assign(&num1, 3.0, 4.0);
    assign(&num2, 1.0, -2.0);

    printf("复数 1: ");
    printComplex(num1);

    printf("复数 2: ");
    printComplex(num2);

    // 加法测试
    add(&result, num1, num2);
    printf("加法结果: ");
    printComplex(result);

    // 乘法测试
    multiply(&result, num1, num2);
    printf("乘法结果: ");
    printComplex(result);

    return 0;
}