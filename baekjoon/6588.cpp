/*
    6588 : 골드바흐의 추측
    URL : https://www.acmicpc.net/problem/6588
    Input :
        8
        20
        42
        0
    Output :
        8 = 3 + 5
        20 = 3 + 17
        42 = 5 + 37
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>

#define MAX_N 1000001

using namespace std;

bool primes[MAX_N];

int main(int argc, char const *argv[])
{
    int n;

    memset(&(primes[0]), false, sizeof(bool) * MAX_N);

    for (int i = 3; i < MAX_N; i += 2)
    {
        bool prime = true;

        for (int j = 3; j <= sqrt(i); j++)
        {
            if ((i % j) == 0)
            {
                prime = false;
                break;
            }
        }

        primes[i] = prime;
    }

    while (true)
    {
        scanf("%d", &n);
        if (n == 0)
        {
            break;
        }

        int a = 0;
        int b = 0;
        for (int i = (n - 1); i > 2; i -= 2)
        {
            a = n - i;
            b = i;

            if (primes[a] && primes[b])
            {
                break;
            }

            a = 0;
            b = 0;
        }

        if ((a != 0) && (b != 0))
        {
            printf("%d = %d + %d\n", n, a, b);
        }
        else
        {
            printf("Goldbach's conjecture is wrong.\n");
        }
    }

    return 0;
}
