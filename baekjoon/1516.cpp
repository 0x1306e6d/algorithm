/*
    1516 : 게임 개발
    URL : https://www.acmicpc.net/problem/1516
    Input :
        5
        10 -1
        10 1 -1
        4 1 -1
        4 3 1 -1
        3 3 -1
    Output :
        10
        20
        14
        18
        17
*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

int n;
std::vector<int> times;
std::vector<int> indegree;
std::vector<std::vector<int>> adjacents;
std::vector<int> answers;

void tsort()
{
    std::queue<int> q;

    for (int i = 0; i < n; i++)
    {
        if (indegree[i] == 0)
        {
            q.push(i);
            answers[i] = times[i];
        }
    }

    while (!q.empty())
    {
        int here = q.front();
        q.pop();

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int there = adjacents[here][i];

            if (indegree[there] > 0)
            {
                answers[there] = std::max(answers[there],
                                          answers[here] + times[there]);

                indegree[there]--;
                if (indegree[there] == 0)
                {
                    q.push(there);
                }
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    std::cin >> n;

    times = std::vector<int>(n, 0);
    indegree = std::vector<int>(n, 0);
    adjacents = std::vector<std::vector<int>>(n, std::vector<int>());
    answers = std::vector<int>(n, 0);

    for (int i = 0; i < n; i++)
    {
        std::cin >> times[i];

        while (true)
        {
            int requirement;
            std::cin >> requirement;

            if (requirement == -1)
            {
                break;
            }
            else
            {
                indegree[i]++;
                adjacents[requirement - 1].push_back(i);
            }
        }
    }

    tsort();

    for (int i = 0; i < n; i++)
    {
        std::cout << answers[i] << std::endl;
    }

    return 0;
}
