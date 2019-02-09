/*
    111401 :  이항 계수 3
    URL : https://www.acmicpc.net/problem/11401
    Input :
        5 2
    Output :
        10
*/

#include <iostream>
#include <cstdint>

#define MAX_N 4000001
#define MAX_K 4000001

#define MOD 1000000007

uint64_t factorial[MAX_N];
uint64_t inverse[MAX_N];

uint64_t power(uint64_t x, uint64_t y)
{
    uint64_t z = 1;

    while (y > 0)
    {
        if (y % 2)
        {
            z = (z * x) % MOD;
        }

        x = (x * x) % MOD;
        y /= 2;
    }

    return z;
}

int main(int argc, char const *argv[])
{
    int N;
    int K;

    factorial[0] = 1;
    factorial[1] = 1;
    for (int i = 2; i <= MAX_N; i++)
    {
        factorial[i] = (factorial[i - 1] * i) % MOD;
    }

    inverse[MAX_N] = power(factorial[MAX_N], MOD - 2);
    for (int i = MAX_N - 1; i >= 0; i--)
    {
        inverse[i] = (inverse[i + 1] * (i + 1)) % MOD;
    }

    std::cin >> N;
    std::cin >> K;

    uint64_t b = (factorial[N] * inverse[N - K]) % MOD;
    b = (b * inverse[K]) % MOD;
    std::cout << b;

    return 0;
}
