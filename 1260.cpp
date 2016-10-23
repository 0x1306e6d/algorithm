/*
    1260 : DFS와 BFS 
    URL : https://www.acmicpc.net/problem/1260
    Input :
        4 5 1
        1 2
        1 3
        1 4
        2 4
        3 4
    Output :
        1 2 4 3
        1 2 3 4
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

#define MAX_VERTEX 1001
#define MAX_EDGE 10001
using namespace std;

void DFS(int vertex);
void BFS(int vertex);

int N, M, V;
vector<int> TABLE[MAX_VERTEX];
bool VISITED[MAX_VERTEX];

int main()
{
    cin >> N >> M >> V;

    for (int i = 0; i < M; ++i)
    {
        int a, b;
        cin >> a >> b;
        TABLE[a].push_back(b);
        TABLE[b].push_back(a);
    }
    for (int i = 1; i <= N; ++i)
    {
        sort(TABLE[i].begin(), TABLE[i].end());
    }

    memset(VISITED, false, sizeof(VISITED));
    DFS(V);
    cout << endl;

    memset(VISITED, false, sizeof(VISITED));
    BFS(V);

    return 0;
}

void DFS(int vertex)
{
    cout << vertex << ' ';
    vector<int> nodes = TABLE[vertex];
    VISITED[vertex] = true;

    for (int i = 0; i < nodes.size(); ++i)
    {
        int target = nodes[i];
        if (!VISITED[target])
        {
            DFS(target);
        }
    }
}

void BFS(int vertex)
{
    queue<int> waiting;
    waiting.push(vertex);
    VISITED[vertex] = true;

    while (!waiting.empty())
    {
        int node = waiting.front();
        waiting.pop();
        cout << node << ' ';

        vector<int> nodes = TABLE[node];
        for (int i = 0; i < nodes.size(); ++i)
        {
            int target = nodes[i];
            if (!VISITED[target])
            {
                waiting.push(target);
                VISITED[target] = true;
            }
        }
    }
}