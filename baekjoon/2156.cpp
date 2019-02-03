/*
    2156 : 포도주 시식
    URL : https://www.acmicpc.net/problem/2156
    Input :
        6
        6
        10
        13
        9
        8
        1
    Output :
        33
*/

#include <iostream>
#include <cstring>

#define MAX_N 10001
#define MAX_SEQUENCE 3

using namespace std;

int N;
int WINE[MAX_N];
int CACHE[MAX_N][MAX_SEQUENCE];

int main(int argc, char const *argv[])
{
    memset(&(CACHE[0][0]), 0, sizeof(int) * MAX_N * MAX_SEQUENCE);

    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> WINE[i];
    }

    CACHE[1][1] = WINE[1];
    CACHE[2][0] = WINE[1];
    CACHE[2][1] = WINE[2];
    CACHE[2][2] = WINE[1] + WINE[2];

    for (int i = 3; i <= N; i++)
    {
        CACHE[i][0] = max(CACHE[i - 1][0],
                          max(CACHE[i - 1][1], CACHE[i - 1][2]));
        CACHE[i][1] = CACHE[i - 1][0] + WINE[i];
        CACHE[i][2] = CACHE[i - 1][1] + WINE[i];
    }

    cout << max(CACHE[N][0], max(CACHE[N][1], CACHE[N][2]));

    return 0;
}
