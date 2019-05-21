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
#include <vector>

std::vector<int> times;
std::vector<std::vector<int>> adjacents;
std::vector<int> answers;

void dfs(int here, int time)
{
    answers[here] += time;

    for (int i = 0; i < adjacents[here].size(); i++)
    {
        dfs(adjacents[here][i], time);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    times = std::vector<int>(n, 0);
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
                adjacents[requirement - 1].push_back(i);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        dfs(i, times[i]);
    }

    for (int i = 0; i < n; i++)
    {
        std::cout << answers[i] << std::endl;
    }

    return 0;
}
