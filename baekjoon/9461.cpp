/*
    9461 : 파도반 수열
    URL : https://www.acmicpc.net/problem/9461
    Input :
        2
        6
        12
    Output :
        3
        16
*/

#include <iostream>
#include <cstdint>
#include <cstring>

#define MAX_N 101

uint64_t cache[MAX_N];

uint64_t P(int n)
{
    if (n < 1)
    {
        return 0;
    }

    uint64_t &ret = cache[n];
    if (ret != -1)
    {
        return ret;
    }

    int i = n - 1;
    int j = n - 5;
    ret = P(i) + P(j);
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0]), -1, sizeof(uint64_t) * MAX_N);
    cache[1] = 1;
    cache[2] = 1;
    cache[3] = 1;
    cache[4] = 2;
    cache[5] = 2;
    cache[6] = 3;
    cache[7] = 4;
    cache[8] = 5;
    cache[9] = 7;
    cache[10] = 9;

    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        int N;
        std::cin >> N;
        std::cout << P(N) << std::endl;
    }

    return 0;
}
