/*
    10844 : 쉬운 계단 수
    URL : https://www.acmicpc.net/problem/10844
    Input #1 :
        1
    Output #1 :
        9
    Input #2 :
        2
    Output #2 :
        17
*/
#include <iostream>
#include <cstring>

#define MOD 1000000000

#define MAX_N 101
#define MAX_I 11

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    int cache[MAX_N][MAX_I];

    memset(&(cache[0][0]), 0, sizeof(int) * MAX_N * MAX_I);

    cin >> N;

    for (int i = 1; i < 10; i++)
    {
        cache[1][i] = 1;
    }

    for (int i = 2; i <= N; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            switch (j)
            {
            case 0:
                cache[i][j + 1] += cache[i - 1][j];
                cache[i][j + 1] %= MOD;
                break;
            case 9:
                cache[i][j - 1] += cache[i - 1][j];
                cache[i][j - 1] %= MOD;
                break;
            default:
                cache[i][j - 1] += cache[i - 1][j];
                cache[i][j + 1] += cache[i - 1][j];
                cache[i][j + 1] %= MOD;
                cache[i][j - 1] %= MOD;
                break;
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 10; i++)
    {
        count = ((count + cache[N][i]) % MOD);
    }
    cout << count;

    return 0;
}
