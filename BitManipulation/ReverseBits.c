// 190 Reverse Bits
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

uint32_t reverseBits(uint32_t n)
{
    uint32_t res = 0;
    for (int i = 0; i < 32; i++)
    {
        res += (n & 1) * (int)pow(2, 31 - i);
        n = n >> 1;
    }

    return res;
}

int main()
{

    int n = 0b0000010100101000001111010011100;

    printf("\n%d", reverseBits(n));

    return 0;
}