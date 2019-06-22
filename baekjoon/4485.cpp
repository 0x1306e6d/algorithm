/*
    4485 : 녹색 옷 입은 애가 젤다지?
    URL : https://www.acmicpc.net/problem/4485
    Input :
        3
        5 5 4
        3 9 1
        3 2 7
        5
        3 7 2 0 1
        2 8 0 9 1
        1 2 1 8 1
        9 8 9 2 0
        3 6 5 1 5
        7
        9 0 5 1 1 5 3
        4 1 2 1 6 5 3
        0 7 6 1 6 8 5
        1 1 7 8 3 2 3
        9 4 0 7 6 4 1
        5 8 3 2 4 8 3
        7 4 8 4 8 3 4
        0
    Output :
        Problem 1: 20
        Problem 2: 19
        Problem 3: 36
*/

#include <iostream>
#include <queue>

#define MAX_N 126
#define INF 987654321

const int dx[] = {0, 0, -1, 1};
const int dy[] = {-1, 1, 0, 0};

int rupee[MAX_N][MAX_N];
int cost[MAX_N][MAX_N];

int main(int argc, char const *argv[])
{
    int t = 0;

    while (++t)
    {
        int n;
        std::cin >> n;
        if (n == 0)
        {
            break;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                std::cin >> rupee[i][j];
                cost[i][j] = INF;
            }
        }

        cost[0][0] = rupee[0][0];

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
                int nextCost = (cost[y][x] + rupee[nextY][nextX]);

                if ((nextX < 0) || (nextY < 0) || (nextX >= n) || (nextY >= n))
                {
                    continue;
                }

                if (cost[nextY][nextX] > nextCost)
                {
                    cost[nextY][nextX] = nextCost;
                    q.push(std::make_pair(nextX, nextY));
                }
            }
        }

        printf("Problem %d: %d\n", t, cost[n - 1][n - 1]);
    }

    return 0;
}
