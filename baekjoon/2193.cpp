/*
    2193 : 이친수
    URL : https://www.acmicpc.net/problem/2193
    Input :
        3
    Output :
        2
*/

#include <iostream>
#include <cstdint>

#define MAX_N 91
#define MAX_PINARY 2

using namespace std;

uint64_t pinary(int n)
{
    uint64_t cache[MAX_N][MAX_PINARY];

    cache[1][0] = 0;
    cache[1][1] = 1;

    for (int i = 2; i <= n; i++)
    {
        cache[i][0] = cache[i - 1][0] + cache[i - 1][1];
        cache[i][1] = cache[i - 1][0];
    }

    return cache[n][0] + cache[n][1];
}

int main(int argc, char const *argv[])
{
    int N;

    cin >> N;
    cout << pinary(N);

    return 0;
}
