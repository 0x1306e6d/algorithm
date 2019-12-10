/*
    1010: 다리 놓기
    URL: https://www.acmicpc.net/problem/1010
    Input:
        3
        2 2
        1 5
        13 29
    Output:
        1
        5
        67863915
*/

#include <iostream>
#include <cstring>

#define MAX_N 31

int cache[MAX_N][MAX_N];

int combination(int n, int k)
{
    if (n == 1)
    {
        return k;
    }
    if (k == 1)
    {
        return n;
    }
    if (n == k)
    {
        return 1;
    }

    int &ret = cache[n][k];
    if (ret != -1)
    {
        return ret;
    }

    ret = combination(n - 1, k - 1) + combination(n - 1, k);
    return ret;
}

int main(int argc, char const *argv[])
{
    int t;
    std::cin >> t;

    while (t--)
    {
        std::memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        int n;
        int m;
        std::cin >> n;
        std::cin >> m;

        std::cout << combination(m, n) << std::endl;
    }

    return 0;
}
