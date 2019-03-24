/*
    1520 : 내리막 길
    URL : https://www.acmicpc.net/problem/1520
    Input :
        4 5
        50 45 37 32 30
        35 50 40 20 25
        30 30 25 17 28
        27 24 22 15 10
    Output :
        3
*/

#include <iostream>
#include <cstring>

#define MAX_M 501
#define MAX_N 501

int m;
int n;
int board[MAX_M][MAX_N];
int path[MAX_M][MAX_N];

int find(int y, int x)
{
    int &ret = path[y][x];
    if (ret != -1)
    {
        return ret;
    }

    if ((y < 0) || (y >= m))
    {
        return 0;
    }
    if ((x < 0) || (x >= n))
    {
        return 0;
    }
    if ((y == (m - 1)) && (x == (n - 1)))
    {
        return 1;
    }

    ret = 0;
    if ((y - 1) >= 0) // top
    {
        if (board[y - 1][x] < board[y][x])
        {
            ret += find(y - 1, x);
        }
    }
    if ((y + 1) < m) // bottom
    {
        if (board[y + 1][x] < board[y][x])
        {
            ret += find(y + 1, x);
        }
    }
    if ((x - 1) >= 0) // left
    {
        if (board[y][x - 1] < board[y][x])
        {
            ret += find(y, x - 1);
        }
    }
    if ((x + 1) < n) // right
    {
        if (board[y][x + 1] < board[y][x])
        {
            ret += find(y, x + 1);
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(path[0][0]), -1, sizeof(int) * MAX_M * MAX_N);

    std::cin >> m;
    std::cin >> n;

    for (int y = 0; y < m; y++)
    {
        for (int x = 0; x < n; x++)
        {
            std::cin >> board[y][x];
        }
    }

    std::cout << find(0, 0);

    return 0;
}
