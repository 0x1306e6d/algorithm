/*
    1890 : 점프
    URL : https://www.acmicpc.net/problem/1890
    Input :
        4
        2 3 3 1
        1 2 1 3
        1 2 3 1
        3 1 1 0
    Output :
        3
*/

#include <iostream>
#include <cstdint>
#include <cstring>
#include <vector>

#define MAX_N 101

int n;
uint64_t cache[MAX_N][MAX_N];
std::vector<std::pair<int, int>> board[MAX_N][MAX_N];

uint64_t dfs(int x, int y)
{
    if ((x == (n - 1)) && (y == (n - 1)))
    {
        return 1;
    }

    uint64_t &count = cache[y][x];
    if (count != -1)
    {
        return count;
    }

    count = 0;
    std::vector<std::pair<int, int>> links = board[y][x];
    for (int i = 0; i < links.size(); i++)
    {
        count += dfs(links[i].first, links[i].second);
    }
    return count;
}

int main(int argc, char const *argv[])
{
    std::cin >> n;

    memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            int r;
            std::cin >> r;

            if (r == 0)
            {
                continue;
            }

            if ((x + r) < n)
            {
                board[y][x].push_back(std::make_pair(x + r, y));
            }
            if ((y + r) < n)
            {
                board[y][x].push_back(std::make_pair(x, y + r));
            }
        }
    }

    std::cout << dfs(0, 0);

    return 0;
}
