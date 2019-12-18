/*
    5567 : 결혼식
    URL : https://www.acmicpc.net/problem/5567
    Input :
        6
        5
        1 2
        1 3
        3 4
        2 3
        4 5
    Output :
        3
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 501

std::vector<int> people[MAX_N];
bool visited[MAX_N];

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

        people[a].push_back(b);
        people[b].push_back(a);
    }

    int count = 0;
    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(1, 0));
    visited[1] = true;
    while (!q.empty())
    {
        std::pair<int, int> relation = q.front();
        q.pop();

        count++;

        if (relation.second >= 2)
        {
            continue;
        }

        std::vector<int> friends = people[relation.first];
        for (std::vector<int>::iterator it = friends.begin(); it != friends.end(); ++it)
        {
            int f = (*it);
            if (!visited[f])
            {
                visited[f] = true;
                q.push(std::make_pair(f, relation.second + 1));
            }
        }
    }

    std::cout << (count - 1);

    return 0;
}
