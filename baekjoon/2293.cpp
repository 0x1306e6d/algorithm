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
#include <algorithm>

#define MAX_N 101

int coins[MAX_N];

int solve(int k, int i)
{
    if ((k < 0) || (i < 0))
    {
        return 0;
    }

    if (k == 0)
    {
        return 1;
    }

    if (i == 0)
    {
        if (k == coins[i])
        {
            return 1;
        }
        else if (k > coins[i])
        {
            return solve(k - coins[i], i);
        }
    }

    int count = 0;
    int current = k;
    do
    {
        count += solve(current, i - 1);
        current -= coins[i];
    } while (current >= 0);
    return count;
}

int main(int argc, char const *argv[])
{
    int n;
    int k;

    std::cin >> n;
    std::cin >> k;

    for (int i = 0; i < n; i++)
    {
        std::cin >> coins[i];
    }

    std::sort(&(coins[0]), &(coins[1]));
    std::cout << solve(k, n - 1);

    return 0;
}
