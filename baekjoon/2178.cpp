/*
    2178 : 미로 탐색
    URL : https://www.acmicpc.net/problem/2178
    Input #1:
        4 6
        101111
        101010
        101011
        111011
    Output #1:
        15
    Input #2:
        4 6
        110110
        110110
        111111
        111101
    Output #2:
        9
    Input #3:
        2 25
        1011101110111011101110111
        1110111011101110111011101
    Output #3:
        38
    Input #4:
        7 7
        1011111
        1110001
        1000001
        1000001
        1000001
        1000001
        1111111
    Output #4:
        13
*/

#include <iostream>
#include <queue>
#include <string>
#include <vector>

#define MAX_N 101
#define MAX_M 101

struct point
{
    int x;
    int y;
};

int discovered[MAX_N][MAX_M];
std::vector<struct point> maze[MAX_N][MAX_M];

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < n; i++)
    {
        int y = i + 1;

        std::string row;
        std::cin >> row;

        for (int j = 0; j < m; j++)
        {
            if (row[j] == '1')
            {
                int x = j + 1;
                struct point p = {x, y};

                if (x > 1)
                {
                    maze[y][x - 1].push_back(p);
                }
                if (x < m)
                {
                    maze[y][x + 1].push_back(p);
                }
                if (y > 1)
                {
                    maze[y - 1][x].push_back(p);
                }
                if (y < n)
                {
                    maze[y + 1][x].push_back(p);
                }
            }
        }
    }

    std::queue<struct point> q;
    q.push({1, 1});
    discovered[1][1] = 1;
    while (!q.empty())
    {
        struct point p = q.front();
        q.pop();

        std::vector<struct point> nexts = maze[p.y][p.x];
        for (int i = 0; i < nexts.size(); i++)
        {
            struct point next = nexts[i];
            if ((next.y == n) && (next.x == m))
            {
                std::cout << discovered[p.y][p.x] + 1;
                return 0;
            }
            else
            {
                if (discovered[next.y][next.x] == 0)
                {
                    discovered[next.y][next.x] = discovered[p.y][p.x] + 1;
                    q.push(next);
                }
            }
        }
    }

    return 0;
}
