// 371. Sum of Two Integers

#include <stdio.h>

int getSum(int a, int b)
{
    while (b != 0)
    {
        unsigned long carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}

int main()
{

    int x = getSum(-5, 2);
    printf("Value: %d", x);

    return 0;
}