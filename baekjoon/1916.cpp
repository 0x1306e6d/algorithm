/*
    1916 : 최소비용 구하기
    URL : https://www.acmicpc.net/problem/1916
    Input :
        5
        8
        1 2 2
        1 3 3
        1 4 1
        1 5 10
        2 4 2
        3 4 1
        3 5 1
        4 5 3
        1 5
    Output :
        4
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 1001
#define INF 1234567890

int n;
int m;
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
    scanf("%d", &n);

    scanf("%d", &m);

    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        int w;
        scanf("%d %d %d", &a, &b, &w);

        adjacents[a].push_back(std::make_pair(w, b));
    }

    int start;
    int end;
    scanf("%d %d", &start, &end);

    std::vector<int> d = dijikstra(start);
    printf("%d", d[end]);

    return 0;
}
