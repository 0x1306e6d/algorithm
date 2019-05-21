/*
    2252 : 줄 세우기
    URL : https://www.acmicpc.net/problem/2252
    Input #1 :
        3 2
        1 3
        2 3
    Output #1 :
        1 2 3
    Input #2 :
        4 2
        4 2
        3 1
    Output #2 :
        4 2 3 1
*/

#include <iostream>
#include <algorithm>
#include <vector>

int n;
std::vector<std::vector<int>> adjacents;
std::vector<bool> visited;
std::vector<int> order;

void dfs(int here)
{
    visited[here] = true;

    for (int i = 0; i < adjacents[here].size(); i++)
    {
        int there = adjacents[here][i];

        if (!visited[there])
        {
            dfs(there);
        }
    }

    order.push_back(here);
}

int main(int argc, char const *argv[])
{
    std::cin >> n;

    adjacents = std::vector<std::vector<int>>(n, std::vector<int>());
    visited = std::vector<bool>(n, false);

    int m;
    std::cin >> m;
    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        std::cin >> a;
        std::cin >> b;

        adjacents[a - 1].push_back(b - 1);
    }

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            dfs(i);
        }
    }
    std::reverse(order.begin(), order.end());

    for (int i = 0; i < n; i++)
    {
        std::cout << (order[i] + 1) << " ";
    }

    return 0;
}
