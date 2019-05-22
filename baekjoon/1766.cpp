/*
    1766 : 문제집
    URL : https://www.acmicpc.net/problem/1766
    Input :
        4 2
        4 2
        3 1
    Output :
        3 1 4 2
*/

#include <iostream>
#include <queue>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    std::vector<int> indegree(n, 0);
    std::vector<std::vector<int>> adjacents(n, std::vector<int>());
    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        std::cin >> a;
        std::cin >> b;

        indegree[b - 1]++;
        adjacents[a - 1].push_back(b - 1);
    }

    std::priority_queue<int, std::vector<int>, std::greater<int>> q;
    std::vector<int> order;
    for (int i = 0; i < n; i++)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
        }
    }

    while (!q.empty())
    {
        int here = q.top();
        q.pop();

        order.push_back(here);

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int there = adjacents[here][i];

            indegree[there]--;
            if (indegree[there] == 0)
            {
                q.push(there);
            }
        }
    }

    for (int i = 0; i < order.size(); i++)
    {
        std::cout << (order[i] + 1) << " ";
    }

    return 0;
}
