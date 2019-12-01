/*
    1699 : 제곱수의 합
    URL : https://www.acmicpc.net/problem/1699
    Input :
        7
    Output :
        4
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 100002

int cache[MAX_N];

int solve(int n)
{
    if (n < 0)
    {
        return 987654321;
    }
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }

    int &ret = cache[n];
    if (ret != -1)
    {
        return ret;
    }

    ret = 987654321;
    int sqrtn = int(std::sqrt(n));
    for (int i = sqrtn; i >= 1; i--)
    {
        if ((i * i) <= n)
        {
            ret = std::min(ret, 1 + solve(n - (i * i)));
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    int n;
    std::cin >> n;

    std::cout << solve(n);

    return 0;
}
