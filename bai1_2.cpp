#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số có phải là số nguyên có 2 chữ số và là bội của 7 hay không
int isMultipleOf7(int num) {
    return (num >= 10 && num <= 99 && num % 7 == 0);
}

// Hàm kiểm tra số có phải là số chính phương hay không
int isPerfectSquare(int num) {
    int sqrtNum = sqrt(num);
    return (sqrtNum * sqrtNum == num);
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
void countAndPrintPerfectSquares(int n) {
    int count = 0;
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
            count++;
        }
    }
    printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
    printf("Cac so nguyen co 2 chu so va la boi cua 7 la:\n");
    for (int i = 10; i <= 99; i++) {
        if (isMultipleOf7(i)) {
            printf("%d ", i);
        }
    }
    printf("\n\n");

    int n;
    printf("Nhap so nguyen duong n: ");
    scanf("%d", &n);
    countAndPrintPerfectSquares(n);

    return 0;
}
