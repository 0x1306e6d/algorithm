/*
    2667 : 단지번호붙이기
    URL : https://www.acmicpc.net/problem/2667
    Input :
        7
        0110100
        0110101
        1110101
        0000111
        0100000
        0111110
        0111000
    Output :
        3
        7
        8
        9
*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>

#define MAX_N 26

int n;
bool map[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

int bfs(int y, int x)
{
    int count = 0;
    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(x, y));

    while (!q.empty())
    {
        std::pair<int, int> p = q.front();
        q.pop();

        count++;

        if ((p.first > 0) &&
            map[p.second][p.first - 1] &&
            !visited[p.second][p.first - 1])
        {
            visited[p.second][p.first - 1] = true;
            q.push(std::make_pair(p.first - 1, p.second));
        }
        if ((p.first < (n - 1)) &&
            map[p.second][p.first + 1] &&
            !visited[p.second][p.first + 1])
        {
            visited[p.second][p.first + 1] = true;
            q.push(std::make_pair(p.first + 1, p.second));
        }
        if ((p.second > 0) &&
            map[p.second - 1][p.first] &&
            !visited[p.second - 1][p.first])
        {
            visited[p.second - 1][p.first] = true;
            q.push(std::make_pair(p.first, p.second - 1));
        }
        if ((p.second < (n - 1)) &&
            map[p.second + 1][p.first] &&
            !visited[p.second + 1][p.first])
        {
            visited[p.second + 1][p.first] = true;
            q.push(std::make_pair(p.first, p.second + 1));
        }
    }

    return count;
}

int main(int argc, char const *argv[])
{
    std::cin >> n;

    for (int y = 0; y < n; y++)
    {
        std::string row;
        std::cin >> row;

        for (int x = 0; x < n; x++)
        {
            map[y][x] = (row[x] == '1');
        }
    }

    std::vector<int> complex;
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            if (map[y][x] && !visited[y][x])
            {
                visited[y][x] = true;
                complex.push_back(bfs(y, x));
            }
        }
    }

    std::sort(complex.begin(), complex.end());

    std::cout << complex.size() << std::endl;
    for (int i = 0; i < complex.size(); i++)
    {
        std::cout << complex[i] << std::endl;
    }

    return 0;
}
