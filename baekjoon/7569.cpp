/*
    7569 : 토마토
    URL : https://www.acmicpc.net/problem/7569
    Input #1 :
        5 3 1
        0 -1 0 0 0
        -1 -1 0 1 1
        0 0 0 1 1
    Output #1 :
        -1
    Input #2 :
        5 3 2
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 1 0 0
        0 0 0 0 0
    Output #2 :
        4
    Input #3 :
        4 3 2
        1 1 1 1
        1 1 1 1
        1 1 1 1
        1 1 1 1
        -1 -1 -1 -1
        1 1 1 -1
    Output #3 :
        0
*/

#include <iostream>
#include <queue>

#define MAX_M 101
#define MAX_N 101
#define MAX_H 101

#define RIPE 1
#define UNRIPE 0
#define BLANK -1

int storage[MAX_H][MAX_N][MAX_M];

struct tomato
{
    int x;
    int y;
    int z;
};

int main(int argc, char const *argv[])
{
    int nunripe = 0;
    std::queue<struct tomato> ripes;

    int m;
    int n;
    int h;
    std::cin >> m;
    std::cin >> n;
    std::cin >> h;

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                int tomato;
                std::cin >> tomato;

                storage[i][j][k] = tomato;

                if (tomato == RIPE)
                {
                    struct tomato t = {k, j, i};
                    ripes.push(t);
                }
                else if (tomato == UNRIPE)
                {
                    nunripe++;
                }
            }
        }
    }

    int day = 0;
    while (nunripe > 0)
    {
        day++;

        int nripe = ripes.size();
        if (nripe == 0)
        {
            std::cout << -1;
            return 0;
        }

        for (int i = 0; i < nripe; i++)
        {
            struct tomato t = ripes.front();
            ripes.pop();

            if (t.x > 0)
            {
                struct tomato ripe = {t.x - 1, t.y, t.z};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
            if (t.x < (m - 1))
            {
                struct tomato ripe = {t.x + 1, t.y, t.z};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
            if (t.y > 0)
            {
                struct tomato ripe = {t.x, t.y - 1, t.z};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
            if (t.y < (n - 1))
            {
                struct tomato ripe = {t.x, t.y + 1, t.z};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
            if (t.z > 0)
            {
                struct tomato ripe = {t.x, t.y, t.z - 1};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
            if (t.z < (h - 1))
            {
                struct tomato ripe = {t.x, t.y, t.z + 1};

                if (storage[ripe.z][ripe.y][ripe.x] == UNRIPE)
                {
                    storage[ripe.z][ripe.y][ripe.x] = RIPE;
                    nunripe--;

                    ripes.push(ripe);
                }
            }
        }
    }

    std::cout << day;

    return 0;
}
