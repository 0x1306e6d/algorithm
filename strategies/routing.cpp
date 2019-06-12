/*
    ROUTING : 신호 라우팅
    Difficulty : 하
    Input :
        1
        7 14
        0 1 1.3
        0 2 1.1
        0 3 1.24
        3 4 1.17
        3 5 1.24
        3 1 2
        1 2 1.31
        1 2 1.26
        1 4 1.11
        1 5 1.37
        5 4 1.24
        4 6 1.77
        5 6 1.11
        2 6 1.2
    Output :
        1.3200000000
*/

#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>
#include <vector>

#define MAX_N 10001

int n;
int m;
std::vector<std::pair<double, int>> adjacents[MAX_N];

std::vector<double> dijkstra(int s)
{
    std::vector<double> dist(n, std::numeric_limits<double>::max());
    dist[s] = (double)1;

    std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int>>, std::greater<std::pair<double, int>>> pq;
    pq.push(std::make_pair((double)1, s));
    while (!pq.empty())
    {
        double distance = pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if (dist[here] < distance)
        {
            continue;
        }

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int there = adjacents[here][i].second;
            double nextDistance = distance * adjacents[here][i].first;

            if (dist[there] > nextDistance)
            {
                dist[there] = nextDistance;
                pq.push(std::make_pair(nextDistance, there));
            }
        }
    }

    return dist;
}

int main(int argc, char const *argv[])
{
    std::cout << std::fixed;
    std::cout.precision(10);

    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        std::cin >> n;
        std::cin >> m;

        for (int i = 0; i < n; i++)
        {
            adjacents[i].clear();
        }

        for (int i = 0; i < m; i++)
        {
            int a;
            int b;
            double c;
            std::cin >> a;
            std::cin >> b;
            std::cin >> c;

            adjacents[a].push_back(std::make_pair(c, b));
            adjacents[b].push_back(std::make_pair(c, a));
        }

        std::cout << dijkstra(0)[n - 1] << std::endl;
    }

    return 0;
}
