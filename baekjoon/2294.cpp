/*
    2294 : 동전 2
    URL : https://www.acmicpc.net/problem/2294
    Input :
        3 15
        1
        5
        12
    Output :
        3
*/

#include <iostream>
#include <cstring>

#define MAX_N 101
#define MAX_K 10001

int coins[MAX_N];
int cache[MAX_N][MAX_K];

int coin(int i, int n, int k)
{
    if (k == 0)
    {
        return 0;
    }
    if ((i >= n) || (k < 0))
    {
        return MAX_N * MAX_K;
    }

    int &count = cache[i][k];
    if (count != -1)
    {
        return count;
    }

    count = MAX_N * MAX_K;
    int j = 0;
    int remaining = k;
    do
    {
        count = std::min(count, j + coin(i + 1, n, remaining));
        j++;
        remaining -= coins[i];
    } while (remaining >= 0);

    return count;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_K);

    int n;
    int k;
    std::cin >> n;
    std::cin >> k;

    for (int i = 0; i < n; i++)
    {
        std::cin >> coins[i];
    }

    int count = coin(0, n, k);
    if (count == (MAX_N * MAX_K))
    {
        std::cout << -1;
    }
    else
    {
        std::cout << count;
    }

    return 0;
}
