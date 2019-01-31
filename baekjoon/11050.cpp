/*
    11050 : 이항 계수 1
    URL : https://www.acmicpc.net/problem/11050
    Input :
        5 2
    Output :
        10
*/

#include <iostream>
#include <cstdint>
#include <cstring>

#define MAX_N 1001
#define MAX_K 1001

using namespace std;

uint64_t cache[MAX_N][MAX_K];

uint64_t binomial(int n, int k)
{
    uint64_t &ret = cache[n][k];

    if (ret != -1)
    {
        return ret;
    }

    if (k == 0 || k == n)
    {
        return 1;
    }

    ret = binomial(n - 1, k - 1) + binomial(n - 1, k);
    return ret;
}

int main(int argc, char const *argv[])
{
    int N;
    int K;

    memset(&(cache[0]), -1, sizeof(uint64_t) * MAX_N * MAX_K);
    cache[0][0] = 1;
    cache[1][0] = 1;
    cache[1][1] = 1;

    cin >> N;
    cin >> K;

    cout << binomial(N, K);

    return 0;
}
