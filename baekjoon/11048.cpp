/*
    11048 : 이동하기
    URL : https://www.acmicpc.net/problem/11048
    Input #1 :
        3 4
        1 2 3 4
        0 0 0 5
        9 8 7 6
    Output #1 :
        31
    Input #2 :
        3 3
        1 0 0
        0 1 0
        0 0 1
    Output #2 :
        3
    Input #3 :
        4 3
        1 2 3
        6 5 4
        7 8 9
        12 11 10
    Output #3 :
        47
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001
#define MAX_M 1001

int n;
int m;

int maze[MAX_N][MAX_M];
int dp[MAX_N][MAX_M];

int move(int x, int y)
{
    if (x >= m)
    {
        return 0;
    }

    if (y >= n)
    {
        return 0;
    }

    if (dp[y][x] != -1)
    {
        return dp[y][x];
    }

    dp[y][x] = maze[y][x];
    dp[y][x] += std::max(move(x + 1, y),
                         std::max(move(x, y + 1), move(x + 1, y + 1)));
    return dp[y][x];
}

int main(int argc, char const *argv[])
{
    std::memset(&(dp[0][0]), -1, sizeof(int) * MAX_N * MAX_M);

    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cin >> maze[i][j];
        }
    }

    std::cout << move(0, 0);

    return 0;
}
