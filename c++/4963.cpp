/*
    4963 : 섬의 개수
    URL : https://www.acmicpc.net/problem/4963
    Input :
        1 1
        0
        2 2
        0 1
        1 0
        3 2
        1 1 1
        1 1 1
        5 4
        1 0 1 0 0
        1 0 0 0 0
        1 0 1 0 1
        1 0 0 1 0
        5 4
        1 1 1 0 1
        1 0 1 0 1
        1 0 1 0 1
        1 0 1 1 1
        5 5
        1 0 1 0 1
        0 0 0 0 0
        1 0 1 0 1
        0 0 0 0 0
        1 0 1 0 1
        0 0
    Output :
        0
        1
        1
        3
        1
        9
*/
#include <iostream>
#include <string.h>

#define MAX 50
using namespace std;

void search(int x, int y);

int w, h;
int TABLE[MAX][MAX];
bool VISITED[MAX][MAX];

int main()
{
    while (true)
    {        
        scanf("%d %d", &w, &h);

        if (w == 0 && h == 0)
        {
            break;
        }

        memset(TABLE, 0, sizeof(TABLE));
        memset(VISITED, false, sizeof(VISITED));

        for (int i = 0; i < h; ++i)
        {
            for (int j = 0; j < w; ++j)
            {
                scanf("%d", &TABLE[j][i]);
            }
        }

        int count = 0;
        for (int i = 0; i < h; ++i)
        {
            for (int j = 0; j < w; ++j)
            {
                if (TABLE[j][i] == 0 || VISITED[j][i])
                {
                    continue;
                }
                search(j, i);
                count++;
            }
        }
        printf("%d\n", count);
    }
    
    return 0;
}

void search(int x, int y)
{
    if (VISITED[x][y])
    {
        return;
    }
    VISITED[x][y] = true;
    
    int top = y - 1;
    int bottom = y + 1;    
    int left = x - 1;
    int right = x + 1;
    
    if (right < w)
    {
        if (TABLE[right][y] == 1)
        {
            search(right, y);
        }
        if (top >= 0)
        {
            if (TABLE[right][top] == 1)
            {
                search(right, top);
            }
        }
        if (bottom < h)
        {
            if (TABLE[right][bottom] == 1)
            {
                search(right, bottom);
            }
        }
    }
    if (left >= 0)
    {
        if (TABLE[left][y] == 1)
        {
            search(left, y);
        }
        if (top >= 0)
        {
            if (TABLE[left][top] == 1)
            {
                search(left, top);
            }
        }
        if (bottom < h)
        {
            if (TABLE[left][bottom] == 1)
            {
                search(left, bottom);
            }
        }
    }
    if (top >= 0)
    {
        if (TABLE[x][top] == 1)
        {
            search(x, top);
        }
    }
    if (bottom < h)
    {
        if (TABLE[x][bottom] == 1)
        {
            search(x, bottom);
        }
    }
}