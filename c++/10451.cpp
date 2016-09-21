/*
    10461 : 순열 사이클  
    URL : https://www.acmicpc.net/problem/10451
    Input :
        2
        8
        3 2 7 8 1 4 5 6
        10
        2 1 3 4 5 6 7 9 10 8
    Output : 
        3
        7
*/
#include <iostream>
#include <string.h>

#define MAX 1001
using namespace std;

bool DFS(int vertex);

int N;
int TABLE[MAX];
bool VISITED[MAX];

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        memset(TABLE, 0, sizeof(TABLE));
        memset(VISITED, false, sizeof(VISITED));

        scanf("%d", &N);

        for (int i = 1; i <= N; ++i)
        {
            int n;
            scanf("%d", &n);

            TABLE[i] = n;
        }

        int count = 0;
        for (int i = 1; i <= N; ++i)
        {
            if (VISITED[i])
            {
                continue;
            }
            if (DFS(i))
            {
                count++;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}

bool DFS(int vertex)
{
    VISITED[vertex] = true;
    int next = TABLE[vertex];

    if (VISITED[next])
    {
        return true;
    }
    else
    {
        return DFS(next);
    }
}