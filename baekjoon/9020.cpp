/*
    9020 : 골드바흐의 추측
    URL : https://www.acmicpc.net/problem/9020
    Input :
        3
        8
        10
        16
    Output :
        3 5
        5 5
        5 11
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 10001

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
    memset(&(PRIME[0]), true, sizeof(bool) * MAX_N);
    PRIME[0] = false;
    PRIME[1] = false;
    PRIME[2] = true;

    eratosthenes(MAX_N);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int n;
        cin >> n;

        int a = 0;
        int b = 0;
        int mid = n / 2;
        for (int i = mid; i >= 2; i--)
        {
            a = i;
            b = n - i;

            if (PRIME[a] && PRIME[b])
            {
                break;
            }
        }

        cout << a << " " << b << endl;
    }

    return 0;
}
