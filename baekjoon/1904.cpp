/*
    1904: 01타일
    URL: https://www.acmicpc.net/problem/1904
    Input #1:
        4
    Output #1:
        5
*/

#include <iostream>
#include <cstring>

#define MOD 15746
#define MAX_N 1000001

int cache[MAX_N];

int count(int n)
{
    if (n <= 0)
    {
        return 0;
    }

    int &ret = cache[n];
    if (ret != -1)
    {
        return ret;
    }

    if (n == 1)
    {
        ret = 1;
    }
    else if (n == 2)
    {
        ret = 2;
    }
    else
    {
        ret = (count(n - 1) + count(n - 2)) % MOD;
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    int n;
    std::cin >> n;

    std::cout << count(n) % MOD;

    return 0;
}
