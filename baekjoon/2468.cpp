/*
    2468: 안전 영역
    URL: https://www.acmicpc.net/problem/2468
    Input #1:
        5
        6 8 2 6 2
        3 2 3 4 6
        6 7 3 3 2
        7 2 5 3 6
        8 9 5 2 7
    Output #1:
        5
*/

#include <iostream>
#include <cstring>
#include <queue>

#define MAX_N 101

struct point
{
    int x;
    int y;
};

int matrix[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

int main(int argc, char const *argv[])
{
    std::queue<struct point> safe;

    int n;
    std::cin >> n;

    int maxLevel = 0;
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            std::cin >> matrix[y][x];

            safe.push({x, y});
            maxLevel = std::max(maxLevel, matrix[y][x]);
        }
    }

    int maxCount = 0;
    for (int level = 0; level <= maxLevel; level++)
    {
        std::memset(&(visited[0][0]), false, sizeof(bool) * MAX_N * MAX_N);

        int count = 0;

        const size_t size = safe.size();
        for (int i = 0; i < size; i++)
        {
            struct point base = safe.front();
            safe.pop();

            if (matrix[base.y][base.x] > level)
            {
                safe.push(base);
            }
            else
            {
                continue;
            }

            if (visited[base.y][base.x])
            {
                continue;
            }

            std::queue<struct point> q;
            q.push(base);
            visited[base.y][base.x] = true;
            while (!q.empty())
            {
                struct point p = q.front();
                q.pop();

                const int x = p.x;
                const int y = p.y;

                if ((x > 0) && matrix[y][x - 1] > level)
                {
                    if (!visited[y][x - 1])
                    {
                        visited[y][x - 1] = true;
                        q.push({x - 1, y});
                    }
                }
                if ((x < (n - 1)) && matrix[y][x + 1] > level)
                {
                    if (!visited[y][x + 1])
                    {
                        visited[y][x + 1] = true;
                        q.push({x + 1, y});
                    }
                }
                if ((y > 0) && matrix[y - 1][x] > level)
                {
                    if (!visited[y - 1][x])
                    {
                        visited[y - 1][x] = true;
                        q.push({x, y - 1});
                    }
                }
                if ((y < (n - 1)) && matrix[y + 1][x] > level)
                {
                    if (!visited[y + 1][x])
                    {
                        visited[y + 1][x] = true;
                        q.push({x, y + 1});
                    }
                }
            }

            count++;
        }

        maxCount = std::max(maxCount, count);
    }

    std::cout << maxCount;

    return 0;
}
