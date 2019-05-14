/*
    2606 : 바이러스
    URL : https://www.acmicpc.net/problem/2606
    Input :
        7
        6
        1 2
        2 3
        1 5
        5 2
        5 6
        4 7
    Output :
        4
*/

#include <iostream>
#include <queue>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> computers;
    for (int i = 0; i < n; i++)
    {
        computers.push_back(i);
    }

    int m;
    std::cin >> m;

    std::vector<std::vector<int>> links(n, std::vector<int>());
    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        std::cin >> a;
        std::cin >> b;

        links[a - 1].push_back(b - 1);
        links[b - 1].push_back(a - 1);
    }

    int count = 0;
    std::vector<bool> visited(n, false);
    std::queue<int> q;

    visited[0] = true;
    q.push(0);
    while (!q.empty())
    {
        int computer = q.front();
        q.pop();

        int nlinks = links[computer].size();
        for (int i = 0; i < nlinks; i++)
        {
            int link = links[computer][i];
            if (!visited[link])
            {
                visited[link] = true;
                count++;
                q.push(link);
            }
        }
    }

    std::cout << count;

    return 0;
}
