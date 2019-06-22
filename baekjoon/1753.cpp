/*
    1753 : 최단경로
    URL : https://www.acmicpc.net/problem/1753
    Input :
      5 6
      1
      5 1 1
      1 2 2
      1 3 3
      2 3 4
      2 4 5
      3 4 6
    Output :
      0
      2
      3
      7
      INF
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 20001
#define INF 987654321

int v;
int e;
int k;
std::vector<std::pair<int, int>> adjacents[MAX_N];

std::vector<int> dijikstra(void)
{
    std::vector<int> d(v + 1, INF);
    d[k] = 0;

    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
    pq.push(std::make_pair(0, k));
    while (!pq.empty())
    {
        int weight = pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if (d[here] < weight)
        {
            continue;
        }

        for (int i = 0; i < adjacents[here].size(); i++)
        {
            int there = adjacents[here][i].first;
            int nextWeight = adjacents[here][i].second + weight;

            if (d[there] > nextWeight)
            {
                d[there] = nextWeight;
                pq.push(std::make_pair(nextWeight, there));
            }
        }
    }

    return d;
}

int main(int argc, char const *argv[])
{
    scanf("%d %d", &v, &e);
    scanf("%d", &k);

    for (int i = 0; i < e; i++)
    {
        int u;
        int v;
        int w;
        scanf("%d %d %d", &u, &v, &w);

        adjacents[u].push_back(std::make_pair(v, w));
    }

    std::vector<int> d = dijikstra();
    for (int i = 1; i <= v; i++)
    {
        int s = d[i];
        if (s == INF)
        {
            printf("INF\n");
        }
        else
        {
            printf("%d\n", s);
        }
    }

    return 0;
}
