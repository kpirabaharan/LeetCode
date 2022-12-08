// 190 Reverse Bits
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
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

uint32_t reverseBits2(uint32_t n)
{
    uint32_t res = 0;
    for (int i = 0; i < 32; i++)
    {
        res <<= 1;
        res |= n & 1;
        n >>= 1;
    }
    
    return res;
}

int main()
{
    uint32_t n = 0b0000010100101000001111010011100;
    uint32_t ans;
    clock_t t;
    double time_taken;

    t = clock();
    ans = reverseBits(n);
    t = clock() - t;
    time_taken = ((double)t) / CLOCKS_PER_SEC;
    printf("First - Time: %f seconds, Answer: %d\n", time_taken, ans);

    t = clock();
    ans = reverseBits2(n);
    t = clock() - t;
    time_taken = ((double)t) / CLOCKS_PER_SEC;
    printf("Second - Time: %f seconds, Answer: %d\n", time_taken, ans);

    return 0;
}