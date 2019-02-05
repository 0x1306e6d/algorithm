/*
    2581 : 소수
    URL : https://www.acmicpc.net/problem/2581
    Input #1 :
        60
        100
    Output #1 :
        620
        61
    Input #2 :
        64
        65
    Output #2 :
        -1
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 10001

using namespace std;

int M;
int N;

bool CACHE[MAX_N];

void eratosthenes(int n)
{
    int sqrtn = int(sqrt(n));
    for (int i = 2; i <= sqrtn; i++)
    {
        if (CACHE[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                CACHE[j] = false;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    memset(&(CACHE[0]), true, sizeof(bool) * MAX_N);
    CACHE[0] = false;
    CACHE[1] = false;

    cin >> M;
    cin >> N;

    int primeMin = MAX_N;
    int primeSum = 0;
    for (int i = M; i <= N; i++)
    {
        eratosthenes(i);

        if (CACHE[i])
        {
            if (i < primeMin)
            {
                primeMin = i;
            }

            primeSum += i;
        }
    }

    if (primeSum == 0)
    {
        cout << -1;
    }
    else
    {
        cout << primeSum << endl;
        cout << primeMin;
    }

    return 0;
}
