/*
    1261 : 알고스팟
    URL : https://www.acmicpc.net/problem/1261
    Input #1 :
        3 3
        011
        111
        110
    Output #1 :
        3
    Input #2 :
        4 2
        0001
        1000
    Output #2 :
        0
    Input #3 :
        6 6
        001111
        010000
        001111
        110001
        011010
        100010
    Output #3 :
        2
*/

#include <iostream>
#include <queue>

#define MAX_N 101
#define MAX_M 101
#define INF 987654321

const int dx[] = {0, 0, -1, 1};
const int dy[] = {-1, 1, 0, 0};

int n;
int m;
int maze[MAX_N][MAX_M];
int d[MAX_N][MAX_M];

int main(int argc, char const *argv[])
{
    scanf("%d %d", &m, &n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%1d", &(maze[i][j]));
            d[i][j] = INF;
        }
    }

    d[0][0] = 0;

    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(0, 0));
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nextX = (x + dx[i]);
            int nextY = (y + dy[i]);

            if ((nextX < 0) || (nextY < 0) || (nextX >= m) || (nextY >= n))
            {
                continue;
            }

            if (maze[nextY][nextX] == 1)
            {
                if (d[nextY][nextX] > (d[y][x] + 1))
                {
                    d[nextY][nextX] = d[y][x] + 1;
                    q.push(std::make_pair(nextX, nextY));
                }
            }
            else
            {
                if (d[nextY][nextX] > d[y][x])
                {
                    d[nextY][nextX] = d[y][x];
                    q.push(std::make_pair(nextX, nextY));
                }
            }
        }
    }

    printf("%d", d[n - 1][m - 1]);

    return 0;
}