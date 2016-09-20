/*
    11724 : 연결 요소의 개수
    URL : https://www.acmicpc.net/problem/11724
    Input 1 :
        6 5
        1 2
        2 5
        5 1
        3 4
        4 6
    Output 1 :
        2
    Input 2 :
        6 8
        1 2
        2 5
        5 1
        3 4
        4 6
        5 4
        2 4
        2 3
    Output 2 :
        1
*/
#include <iostream>
#include <vector>
#include <string.h>

#define MAX_VERTEX 1001
using namespace std;

bool DFS(int vertex);

int N;
vector<int> TABLE[MAX_VERTEX];
bool VISITED[MAX_VERTEX];

int main()
{
    int M;
    scanf("%d %d", &N, &M);

    memset(VISITED, false, sizeof(VISITED));

    while (M--)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        TABLE[u].push_back(v);
        TABLE[v].push_back(u);
    }

    int count = 0;
    for (int i = 1; i <= N; ++i)
    {
        if (DFS(i))
        {
            count++;
        }
    }
    printf("%d", count);
    return 0;
}

bool DFS(int vertex)
{
    if (VISITED[vertex])
    {
        return false;
    }
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
    return true;
}