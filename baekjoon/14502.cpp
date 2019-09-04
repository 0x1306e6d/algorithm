/*
    14502: 연구소
    URL: https://www.acmicpc.net/problem/14502
    Input #1:
        7 7
        2 0 0 0 1 1 0
        0 0 1 0 1 2 0
        0 1 1 0 1 0 0
        0 1 0 0 0 0 0
        0 0 0 0 0 1 1
        0 1 0 0 0 0 0
        0 1 0 0 0 0 0
    Output #1:
        27
    Input #2:
        4 6
        0 0 0 0 0 0
        1 0 0 0 0 2
        1 1 1 0 0 2
        0 0 0 0 0 2
    Output #2:
        9
    Input #3:
        8 8
        2 0 0 0 0 0 0 2
        2 0 0 0 0 0 0 2
        2 0 0 0 0 0 0 2
        2 0 0 0 0 0 0 2
        2 0 0 0 0 0 0 2
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
    Output #3:
        3
*/

#include <iostream>
#include <cstring>
#include <queue>
#include <vector>

#define MAX_N 8
#define MAX_M 8

#define ROOM 0
#define WALL 1
#define VIRUS 2

struct point
{
    int x;
    int y;
};

int laboratory[MAX_N][MAX_M];
std::vector<struct point> rooms;
std::vector<struct point> viruses;

int simulate(int n, int m, int i, int j, int k)
{
    const struct point r1 = rooms[i];
    const struct point r2 = rooms[j];
    const struct point r3 = rooms[k];

    int simulation[n][m];
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < m; x++)
        {
            simulation[y][x] = laboratory[y][x];
        }
    }
    simulation[r1.y][r1.x] = WALL;
    simulation[r2.y][r2.x] = WALL;
    simulation[r3.y][r3.x] = WALL;

    std::vector<struct point>::iterator it;
    for (it = viruses.begin(); it != viruses.end(); ++it)
    {
        const struct point virus = *it;

        std::queue<struct point> q;
        q.push({virus.x, virus.y});
        while (!q.empty())
        {
            const struct point p = q.front();
            q.pop();

            const int x = p.x;
            const int y = p.y;

            if ((y > 0) && (simulation[y - 1][x] == ROOM))
            {
                simulation[y - 1][x] = VIRUS;
                q.push({x, y - 1});
            }
            if ((y < (n - 1)) && (simulation[y + 1][x] == ROOM))
            {
                simulation[y + 1][x] = VIRUS;
                q.push({x, y + 1});
            }
            if ((x > 0) && (simulation[y][x - 1] == ROOM))
            {
                simulation[y][x - 1] = VIRUS;
                q.push({x - 1, y});
            }
            if ((x < (m - 1)) && (simulation[y][x + 1] == ROOM))
            {
                simulation[y][x + 1] = VIRUS;
                q.push({x + 1, y});
            }
        }
    }

    int count = 0;
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < m; x++)
        {
            if (simulation[y][x] == ROOM)
            {
                count++;
            }
        }
    }

    return count;
}

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < m; x++)
        {
            std::cin >> laboratory[y][x];

            switch (laboratory[y][x])
            {
            case ROOM:
                rooms.push_back({x, y});
                break;
            case VIRUS:
                viruses.push_back({x, y});
                break;
            }
        }
    }

    int maxCount = 0;
    for (int i = 0; i < rooms.size(); i++)
    {
        for (int j = i + 1; j < rooms.size(); j++)
        {
            for (int k = j + 1; k < rooms.size(); k++)
            {
                int count = simulate(n, m, i, j, k);
                maxCount = std::max(maxCount, count);
            }
        }
    }

    std::cout << maxCount;

    return 0;
}
