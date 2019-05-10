/*
    GALLERY : 감시 카메라 설치
    Difficulty : 중
    Input :
        3
        6 5
        0 1
        1 2
        1 3
        2 5
        0 4
        4 2
        0 1
        2 3
        1000 1
        0 1
    Output :
        3
        2
        999
*/

#include <iostream>
#include <vector>

#define MAX_G 1001

#define UNWATCHED 0
#define WATCHED 1
#define INSTALLED 2

std::vector<int> adjacents[MAX_G];
std::vector<bool> visited;

int installedCamera = 0;

void clear()
{
    for (int i = 0; i < MAX_G; i++)
    {
        adjacents[i].clear();
    }

    visited = std::vector<bool>(MAX_G, false);

    installedCamera = 0;
}

int dfs(int here)
{
    int children[3] = {0, 0, 0};

    visited[here] = true;

    for (int i = 0; i < adjacents[here].size(); i++)
    {
        int there = adjacents[here][i];
        if (!(visited[there]))
        {
            children[dfs(there)]++;
        }
    }

    if (children[UNWATCHED] > 0)
    {
        installedCamera++;
        return INSTALLED;
    }

    if (children[INSTALLED] > 0)
    {
        return WATCHED;
    }

    return UNWATCHED;
}

int installCamera(int g)
{
    for (int u = 0; u < g; u++)
    {
        if (!(visited[u]) && (dfs(u) == UNWATCHED))
        {
            installedCamera++;
        }
    }

    return installedCamera;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        clear();

        int g;
        int h;
        std::cin >> g;
        std::cin >> h;

        for (int i = 0; i < h; i++)
        {
            int g1;
            int g2;
            std::cin >> g1;
            std::cin >> g2;

            adjacents[g1].push_back(g2);
            adjacents[g2].push_back(g1);
        }

        std::cout << installCamera(g) << std::endl;
    }

    return 0;
}
