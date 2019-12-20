/*
    1726 : 로봇
    URL : https://www.acmicpc.net/problem/1726
    Input :
        5 6
        0 0 0 0 0 0
        0 1 1 0 1 0
        0 1 0 0 0 0
        0 0 1 1 1 0
        1 0 0 0 0 0
        4 2 3
        2 4 1
    Output :
        9
*/

#include <iostream>
#include <queue>

#define MAX_N 101
#define MAX_M 101
#define MAX_DIRECTION 5

#define EAST 0
#define WEST 1
#define SOUTH 2
#define NORTH 3

struct movement
{
    int x;
    int y;
    int direction;
    int cost;
};

int m;
int n;
bool factory[MAX_M][MAX_N];
bool visited[MAX_M][MAX_N][MAX_DIRECTION];

int main(int argc, char const *argv[])
{
    std::cin >> m;
    std::cin >> n;

    for (int y = 0; y < m; y++)
    {
        for (int x = 0; x < n; x++)
        {
            std::cin >> factory[y][x];
        }
    }

    int fromX;
    int fromY;
    int fromDirection;
    std::cin >> fromY;
    std::cin >> fromX;
    std::cin >> fromDirection;

    fromX -= 1;
    fromY -= 1;
    fromDirection -= 1;

    int toX;
    int toY;
    int toDirection;
    std::cin >> toY;
    std::cin >> toX;
    std::cin >> toDirection;

    toX -= 1;
    toY -= 1;
    toDirection -= 1;

    visited[fromY][fromX][fromDirection] = true;

    std::queue<struct movement> q;
    q.push({fromX, fromY, fromDirection, 0});
    while (!q.empty())
    {
        struct movement move = q.front();
        q.pop();

        if ((move.x == toX) &&
            (move.y == toY) &&
            (move.direction == toDirection))
        {
            std::cout << move.cost;
            break;
        }

        for (int k = 1; k <= 3; k++)
        {
            int x;
            int y;
            switch (move.direction)
            {
            case EAST:
                x = move.x + k;
                y = move.y;
                break;
            case WEST:
                x = move.x - k;
                y = move.y;
                break;
            case SOUTH:
                x = move.x;
                y = move.y + k;
                break;
            case NORTH:
                x = move.x;
                y = move.y - k;
                break;
            }

            if ((x >= 0) && (x < n) && (y >= 0) && (y < m))
            {
                if (factory[y][x] == 0)
                {
                    if (!visited[y][x][move.direction])
                    {
                        visited[y][x][move.direction] = true;
                        q.push({x, y, move.direction, move.cost + 1});
                    }
                }
                else
                {
                    break;
                }
            }
            else
            {
                break;
            }
        }

        if ((move.direction == EAST) || (move.direction == WEST))
        {
            if (!visited[move.y][move.x][SOUTH])
            {
                visited[move.y][move.x][SOUTH] = true;
                q.push({move.x, move.y, SOUTH, move.cost + 1});
            }
            if (!visited[move.y][move.x][NORTH])
            {
                visited[move.y][move.x][NORTH] = true;
                q.push({move.x, move.y, NORTH, move.cost + 1});
            }
        }
        else if ((move.direction == SOUTH) || (move.direction == NORTH))
        {
            if (!visited[move.y][move.x][EAST])
            {
                visited[move.y][move.x][EAST] = true;
                q.push({move.x, move.y, EAST, move.cost + 1});
            }
            if (!visited[move.y][move.x][WEST])
            {
                visited[move.y][move.x][WEST] = true;
                q.push({move.x, move.y, WEST, move.cost + 1});
            }
        }
    }

    return 0;
}
