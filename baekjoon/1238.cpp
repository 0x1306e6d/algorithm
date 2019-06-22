/*
    1238 : 파티
    URL : https://www.acmicpc.net/problem/1238
    Input :
        4 8 2
        1 2 4
        1 3 2
        1 4 7
        2 1 1
        2 3 5
        3 1 2
        3 4 4
        4 2 3
    Output :
        10
*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 1001
#define INF 987654321

int n;
int m;
int x;
std::vector<std::pair<int, int>> forwardAdjacents[MAX_N];
std::vector<std::pair<int, int>> backwardAdjacents[MAX_N];

std::vector<int> dijikstraForward(int start)
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

        for (int i = 0; i < forwardAdjacents[here].size(); i++)
        {
            int nextDistance = forwardAdjacents[here][i].first + distance;
            int there = forwardAdjacents[here][i].second;

            if (d[there] > nextDistance)
            {
                d[there] = nextDistance;
                pq.push(std::make_pair(nextDistance, there));
            }
        }
    }

    return d;
}

std::vector<int> dijikstraBackward(int start)
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

        for (int i = 0; i < backwardAdjacents[here].size(); i++)
        {
            int nextDistance = backwardAdjacents[here][i].first + distance;
            int there = backwardAdjacents[here][i].second;

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
    scanf("%d %d %d", &n, &m, &x);

    for (int i = 0; i < m; i++)
    {
        int a;
        int b;
        int t;
        scanf("%d %d %d", &a, &b, &t);

        forwardAdjacents[a].push_back(std::make_pair(t, b));
        backwardAdjacents[b].push_back(std::make_pair(t, a));
    }

    std::vector<int> forward = dijikstraForward(x);
    std::vector<int> backward = dijikstraBackward(x);

    int max = 0;
    for (int i = 1; i <= n; i++)
    {
        max = std::max(max, forward[i] + backward[i]);
    }
    printf("%d", max);

    return 0;
}
