/*
    11403 : 경로 찾기
    URL : https://www.acmicpc.net/problem/11403
    Input #1 :
        3
        0 1 0
        0 0 1
        1 0 0
    Output #1 :
        1 1 1
        1 1 1
        1 1 1
    Input #2 :
        7
        0 0 0 1 0 0 0
        0 0 0 0 0 0 1
        0 0 0 0 0 0 0
        0 0 0 0 1 1 0
        1 0 0 0 0 0 0
        0 0 0 0 0 0 1
        0 0 1 0 0 0 0
    Output #2 :
        1 0 1 1 1 1 1
        0 0 1 0 0 0 1
        0 0 0 0 0 0 0
        1 0 1 1 1 1 1
        1 0 1 1 1 1 1
        0 0 1 0 0 0 1
        0 0 1 0 0 0 0
*/

#include <iostream>
#include <cstring>
#include <queue>
#include <vector>

#define MAX_N 101

bool visited[MAX_N];
bool connected[MAX_N][MAX_N];
std::vector<int> links[MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        links[i].clear();

        for (int j = 0; j < n; j++)
        {
            int link;
            std::cin >> link;

            connected[i][j] = (link == 1);

            if (link == 1)
            {
                links[i].push_back(j);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        std::memset(&(visited[0]), false, sizeof(bool) * MAX_N);
        visited[i] = true;

        std::queue<int> q;
        q.push(i);
        while (!q.empty())
        {
            int j = q.front();
            q.pop();

            for (std::vector<int>::iterator it = links[j].begin(); it != links[j].end(); ++it)
            {
                int k = *it;

                connected[i][k] = true;

                if (!visited[k])
                {
                    visited[k] = true;

                    q.push(k);
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            std::cout << connected[i][j];

            if (j < (n - 1))
            {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }

    return 0;
}
