/*
    1325 : 효율적인 해킹
    URL : https://www.acmicpc.net/problem/1325
    Input :
        5 4
        3 1
        3 2
        4 3
        5 3
    Output :
        1 2
*/

#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>

#define MAX_N 10001

bool visited[MAX_N];
std::vector<int> computers[MAX_N];

int dfs(int i)
{
    visited[i] = true;

    int count = 0;
    for (int j = 0; j < computers[i].size(); j++)
    {
        if (!visited[computers[i][j]])
        {
            count += 1 + dfs(computers[i][j]);
        }
    }
    return count;
}

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        std::cin >> a;
        std::cin >> b;

        computers[b - 1].push_back(a - 1);
    }

    int maxCount = 0;
    std::vector<int> counts;
    for (int i = 0; i < n; i++)
    {
        memset(&(visited[0]), false, sizeof(bool) * MAX_N);

        int count = dfs(i);
        if (counts.empty() || (count == maxCount))
        {
            counts.push_back(i + 1);
            maxCount = count;
        }
        else if (count > maxCount)
        {
            counts.clear();
            counts.push_back(i + 1);
            maxCount = count;
        }
    }

    std::sort(counts.begin(), counts.end());

    for (int i = 0; i < counts.size(); i++)
    {
        std::cout << counts[i] << " ";
    }

    return 0;
}
