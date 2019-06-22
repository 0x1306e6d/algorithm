/*
    1504 : 특정한 최단 경로
    URL : https://www.acmicpc.net/problem/1504
    Input :
        4 6
        1 2 3
        2 3 3
        3 4 1
        1 3 5
        2 4 5
        1 4 4
        2 3
    Output :
        7
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 801
#define INF 987654321

int n;
int e;
int u;
int v;
std::vector<std::pair<int, int>> adjacents[MAX_N];

std::vector<int> dijikstra(int start)
{
    std::vector<int> d(n + 1, INF);
    d[start] = 0;

    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
    pq.push(std::make_pair(0, start));
    while (!pq.empty())
    {
        int distance = pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if (d[here] < distance)
        {
            continue;
        }

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int nextDistance = adjacents[here][i].first + distance;
            int there = adjacents[here][i].second;

            if (d[there] > nextDistance)
            {
                d[there] = nextDistance;
                pq.push(std::make_pair(nextDistance, there));
            }
        }
    }

    return d;
}

int main(int argc, char const *argv[])
{
    scanf("%d %d", &n, &e);

    for (int i = 0; i < e; i++)
    {
        int a;
        int b;
        int c;
        scanf("%d %d %d", &a, &b, &c);

        adjacents[a].push_back(std::make_pair(c, b));
        adjacents[b].push_back(std::make_pair(c, a));
    }

    scanf("%d %d", &u, &v);

    std::vector<int> one = dijikstra(1);
    std::vector<int> two = dijikstra(u);
    std::vector<int> three = dijikstra(v);

    int d1 = INF;
    if ((one[u] != INF) && (two[v] != INF) && (three[n] != INF))
    {
        d1 = (one[u] + two[v] + three[n]);
    }

    int d2 = INF;
    if ((one[v] != INF) && (three[u] != INF) && (two[n] != INF))
    {
        d2 = (one[v] + three[u] + two[n]);
    }

    if ((d1 == INF) && (d2 == INF))
    {
        printf("-1");
    }
    else
    {
        printf("%d", std::min(d1, d2));
    }

    return 0;
}
