/*
    1149 : RGB거리
    URL : https://www.acmicpc.net/problem/1149
    Input :
        3
        26 40 83
        49 60 57
        13 89 99
    Output :
        96
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001
#define RGB 3
#define R 0
#define G 1
#define B 2

using namespace std;

int costs[MAX_N][RGB];
int cache[MAX_N][RGB];

int main(int argc, char const *argv[])
{
    int N;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> costs[i][R];
        cin >> costs[i][G];
        cin >> costs[i][B];
    }

    cache[0][R] = costs[0][R];
    cache[0][G] = costs[0][G];
    cache[0][B] = costs[0][B];
    for (int i = 1; i < N; i++)
    {
        cache[i][R] = min(cache[i - 1][G], cache[i - 1][B]) + costs[i][R];
        cache[i][G] = min(cache[i - 1][R], cache[i - 1][B]) + costs[i][G];
        cache[i][B] = min(cache[i - 1][R], cache[i - 1][G]) + costs[i][B];
    }

    cout << min(min(cache[N - 1][R], cache[N - 1][G]), cache[N - 1][B]);

    return 0;
}
