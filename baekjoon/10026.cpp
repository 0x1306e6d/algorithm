/*
    10026 : 적록색약
    URL : https://www.acmicpc.net/problem/10026
    Input :
        5
        RRRBB
        GGBBB
        BBBRR
        BBRRR
        RRRRR
    Output :
        4 3
*/

#include <iostream>
#include <cstring>
#include <queue>
#include <tuple>

#define MAX_N 101

#define R 'R'
#define G 'G'
#define B 'B'

const int dxs[] = {0, 0, -1, 1};
const int dys[] = {-1, 1, 0, 0};

int picture[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::string s;
        std::cin >> s;

        for (int j = 0; j < n; j++)
        {
            picture[i][j] = s.at(j);
        }
    }

    std::queue<std::tuple<int, int, int>> q;

    int normal = 0;
    std::memset(&(visited[0][0]), false, sizeof(bool) * MAX_N * MAX_N);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (visited[i][j])
            {
                continue;
            }

            normal++;
            visited[i][j] = true;
            q.push(std::make_tuple(i, j, picture[i][j]));
            while (!q.empty())
            {
                std::tuple<int, int, int> p = q.front();
                q.pop();

                for (int k = 0; k < 4; k++)
                {
                    int dx = dxs[k];
                    int dy = dys[k];

                    int x = std::get<1>(p) + dx;
                    int y = std::get<0>(p) + dy;
                    if ((x >= 0) && (x < n) && (y >= 0) && (y < n))
                    {
                        if (visited[y][x])
                        {
                            continue;
                        }
                        if (std::get<2>(p) == picture[y][x])
                        {
                            visited[y][x] = true;
                            q.push(std::make_tuple(y, x, picture[y][x]));
                        }
                    }
                }
            }
        }
    }

    std::cout << normal;
    std::cout << " ";

    int abnormal = 0;
    std::memset(&(visited[0][0]), false, sizeof(bool) * MAX_N * MAX_N);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (visited[i][j])
            {
                continue;
            }

            abnormal++;
            visited[i][j] = true;
            q.push(std::make_tuple(i, j, picture[i][j]));
            while (!q.empty())
            {
                std::tuple<int, int, int> p = q.front();
                q.pop();

                for (int k = 0; k < 4; k++)
                {
                    int dx = dxs[k];
                    int dy = dys[k];

                    int x = std::get<1>(p) + dx;
                    int y = std::get<0>(p) + dy;
                    if ((x >= 0) && (x < n) && (y >= 0) && (y < n))
                    {
                        if (visited[y][x])
                        {
                            continue;
                        }
                        if (std::get<2>(p) == picture[y][x])
                        {
                            visited[y][x] = true;
                            q.push(std::make_tuple(y, x, picture[y][x]));
                        }
                        else if ((std::get<2>(p) != B) && (picture[y][x] != B))
                        {
                            visited[y][x] = true;
                            q.push(std::make_tuple(y, x, picture[y][x]));
                        }
                    }
                }
            }
        }
    }

    std::cout << abnormal;

    return 0;
}
