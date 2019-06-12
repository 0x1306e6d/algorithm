/*
    FIRETRUCKS : 소방차
    Difficulty : 중
    Input :
        1
        8 12 3 2
        1 2 3
        1 6 9
        2 3 6
        3 4 4
        3 5 2
        4 5 7
        6 5 5
        8 6 5
        6 7 3
        8 7 3
        7 5 1
        2 8 3
        2 3 5
        4 6
    Output :
        16
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_V 1001
#define INF 987654321

int V;
int E;
int n;
int m;

std::vector<std::pair<int, int>> adjacents[MAX_V];
std::vector<int> destinations;
std::vector<int> stations;

std::vector<int> dijkstra(void)
{
    std::vector<int> dist(V + 1, INF);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;

    for (int i = 0; i < m; i++)
    {
        dist[stations[i]] = 0;
        pq.push(std::make_pair(0, stations[i]));
    }
    while (!pq.empty())
    {
        int distance = pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if (dist[here] < distance)
        {
            continue;
        }

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int there = adjacents[here][i].first;
            int nextDistance = dist[here] + adjacents[here][i].second;

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
    int C;
    std::cin >> C;

    while (C--)
    {
        std::cin >> V;
        std::cin >> E;
        std::cin >> n;
        std::cin >> m;

        for (int i = 0; i < V + 1; i++)
        {
            adjacents[i].clear();
        }
        destinations.clear();
        stations.clear();

        for (int i = 0; i < E; i++)
        {
            int a;
            int b;
            int t;
            std::cin >> a;
            std::cin >> b;
            std::cin >> t;

            adjacents[a].push_back(std::make_pair(b, t));
            adjacents[b].push_back(std::make_pair(a, t));
        }

        for (int i = 0; i < n; i++)
        {
            int a;
            std::cin >> a;

            destinations.push_back(a);
        }

        for (int i = 0; i < m; i++)
        {
            int a;
            std::cin >> a;

            stations.push_back(a);
        }

        std::vector<int> d = dijkstra();
        int sum = 0;
        for (int i = 0; i < destinations.size(); i++)
        {
            sum += d[destinations[i]];
        }
        std::cout << sum << std::endl;
    }

    return 0;
}