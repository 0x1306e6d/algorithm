/*
    1978 : 소수 찾기
    URL : https://www.acmicpc.net/problem/1978
    Input :
        4
        1 3 5 7
    Output :
        3
*/
#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 1001

using namespace std;

bool cache[MAX_N];

void eratosthenes(int n)
{
    cache[0] = false;
    cache[1] = false;

    int sqrtn = int(sqrt(n));
    for (int i = 2; i <= sqrtn; i++)
    {
        if (cache[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                cache[j] = false;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    int N;
    int count = 0;

    memset(&(cache[0]), true, sizeof(bool) * MAX_N);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int n;

        cin >> n;

        eratosthenes(n);

        if (cache[n])
        {
            count += 1;
        }
    }

    cout << count;

    return 0;
}
