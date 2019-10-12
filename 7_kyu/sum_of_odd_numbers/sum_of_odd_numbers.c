#include <inttypes.h>
#include <stdio.h>

uint64_t rowSumOddNumbers(uint32_t n)
{
    uint64_t temp = 2;
    uint64_t sum = 0;
    for (int i = 0; i < n; i++)
    {
        temp = temp + 2 * i;
    }
    uint64_t start = temp - 1;
    for (int k = 0; k < n; k++)
    {
        sum = sum + start + 2 * k;
    }
    return sum;
}
