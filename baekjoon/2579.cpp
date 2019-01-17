/*
    2579 : 계단 오르기
    URL : https://www.acmicpc.net/problem/2579
    Input :
        6
        10
        20
        15
        25
        10
        20
    Output :
        75
*/
#include <iostream>
#include <cstring>

#define MAX_N 302
#define MAX_JUMP 3

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    int stairs[MAX_N];
    int cache[MAX_N][MAX_JUMP];

    memset(&(stairs[0]), 0, sizeof(int) * MAX_N);
    memset(&(cache[0][0]), 0, sizeof(int) * MAX_N * MAX_JUMP);

    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> stairs[i];
    }

    cache[1][1] = stairs[1];
    cache[1][2] = stairs[1];

    for (int i = 2; i <= N; i++)
    {
        cache[i][1] = cache[i - 1][2] + stairs[i];
        cache[i][2] = max(cache[i - 2][1], cache[i - 2][2]) + stairs[i];
    }

    cout << max(cache[N][1], cache[N][2]);

    return 0;
}
