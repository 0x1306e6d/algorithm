/*
    2960 : 에라토스테네스의 체
    URL : https://www.acmicpc.net/problem/2960
    Input :
        10 7
    Output :
        9
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 1001

bool cache[MAX_N];

int eratosthenes(int n, int k)
{
    int count = 0;

    cache[0] = false;
    cache[1] = false;

    for (int i = 2; i <= n; i++)
    {
        if (cache[i])
        {
            for (int j = i; j <= n; j += i)
            {
                if (cache[j])
                {
                    cache[j] = false;
                    count++;
                    if (count == k)
                    {
                        return j;
                    }
                }
            }
        }
    }

    return n;
}

int main(int argc, char const *argv[])
{
    int n;
    int k;
    std::cin >> n;
    std::cin >> k;

    memset(&(cache[0]), true, sizeof(bool) * MAX_N);

    std::cout << eratosthenes(n, k);

    return 0;
}
