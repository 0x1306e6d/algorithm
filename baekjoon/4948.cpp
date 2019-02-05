/*
    4948 : 베르트랑 공준
    URL : https://www.acmicpc.net/problem/4948
    Input :
        1
        10
        13
        100
        1000
        10000
        100000
        0
    Output :
        1
        4
        3
        21
        135
        1033
        8392
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 246913

using namespace std;

bool PRIME[MAX_N];

void eratosthenes(int n)
{
    int sqrtn = int(sqrt(n));
    for (int i = 2; i <= sqrtn; i++)
    {
        if (PRIME[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                PRIME[j] = false;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    int n = MAX_N;

    memset(&(PRIME[0]), true, sizeof(bool) * MAX_N);
    PRIME[0] = false;
    PRIME[1] = false;
    PRIME[2] = true;

    eratosthenes(MAX_N);

    while (true)
    {
        cin >> n;
        if (n == 0)
        {
            break;
        }

        int count = 0;
        for (int i = (n + 1); i <= (2 * n); i++)
        {
            if (PRIME[i])
            {
                count += 1;
            }
        }

        cout << count << endl;
    }

    return 0;
}
