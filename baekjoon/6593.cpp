/*
    6593 : 상범 빌딩
    URL : https://www.acmicpc.net/problem/6593
    Input :
        3 4 5
        S....
        .###.
        .##..
        ###.#

        #####
        #####
        ##.##
        ##...

        #####
        #####
        #.###
        ####E

        1 3 3
        S##
        #E#
        ###

        0 0 0
    Output :
        Escaped in 11 minute(s).
        Trapped!
*/

#include <iostream>
#include <queue>

#define MAX_L 31
#define MAX_R 31
#define MAX_C 31

#define INF 987654321

#define BLOCK '#'
#define EMPTY '.'
#define START 'S'
#define END 'E'

const int dx[] = {-1, 1, 0, 0, 0, 0};
const int dy[] = {0, 0, -1, 1, 0, 0};
const int dz[] = {0, 0, 0, 0, -1, 1};

char building[MAX_L][MAX_R][MAX_C];
int minute[MAX_L][MAX_R][MAX_C];

struct xyz
{
    int x;
    int y;
    int z;
};

int main(int argc, char const *argv[])
{
    int t = 0;

    while (++t)
    {
        int l;
        int r;
        int c;
        std::cin >> l;
        std::cin >> r;
        std::cin >> c;
        if ((l == 0) && (r == 0) && (c == 0))
        {
            break;
        }

        struct xyz start;
        struct xyz end;
        for (int z = 0; z < l; z++)
        {
            for (int y = 0; y < r; y++)
            {
                for (int x = 0; x < c; x++)
                {
                    std::cin >> building[z][y][x];
                    if (building[z][y][x] == START)
                    {
                        start.x = x;
                        start.y = y;
                        start.z = z;

                        minute[z][y][x] = 0;
                    }
                    else
                    {
                        if (building[z][y][x] == END)
                        {
                            end.x = x;
                            end.y = y;
                            end.z = z;
                        }

                        minute[z][y][x] = INF;
                    }
                }
            }
        }

        std::queue<struct xyz> q;
        q.push(start);
        while (!q.empty())
        {
            int x = q.front().x;
            int y = q.front().y;
            int z = q.front().z;
            q.pop();

            for (int i = 0; i < 6; i++)
            {
                int nextX = (x + dx[i]);
                int nextY = (y + dy[i]);
                int nextZ = (z + dz[i]);

                if ((nextX < 0) || (nextY < 0) || (nextZ < 0) ||
                    (nextX >= c) || (nextY >= r) || (nextZ >= l))
                {
                    continue;
                }

                if (building[nextZ][nextY][nextX] == BLOCK)
                {
                    continue;
                }

                int nextMinute = (minute[z][y][x] + 1);
                if (minute[nextZ][nextY][nextX] > nextMinute)
                {
                    minute[nextZ][nextY][nextX] = nextMinute;
                    q.push({nextX, nextY, nextZ});
                }
            }
        }

        if (minute[end.z][end.y][end.x] == INF)
        {
            printf("Trapped!\n");
        }
        else
        {
            printf("Escaped in %d minute(s).\n", minute[end.z][end.y][end.x]);
        }
    }

    return 0;
}
