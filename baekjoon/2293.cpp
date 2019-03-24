/*
    2293 : 동전 1
    URL : https://www.acmicpc.net/problem/2293
    Input :
        3 10
        1
        2
        5
    Output :
        10
*/

#include <iostream>

#define MAX_N 101
#define MAX_K 10001

int n;
int k;
int coins[MAX_N];
int cache[MAX_K];

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> k;

    for (int i = 0; i < n; i++)
    {
        std::cin >> coins[i];
    }

    cache[0] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = coins[i]; j <= k; j++)
        {
            cache[j] += cache[j - coins[i]];
        }
    }

    std::cout << cache[k];

    return 0;
}
