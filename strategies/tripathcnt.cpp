/*
    TRIPATHCNT : 삼각형 위의 최대 경로 수 세기
    Difficulty : 중
    Input :
        2
        4
        1
        1 1 
        1 1 1 
        1 1 1 1 
        4
        9
        5 7
        1 3 2
        3 5 5 6
    Output :
        8
        3
*/
#include <iostream>
#include <cstring>

#define MAX_N 101

using namespace std;

int triangle[MAX_N][MAX_N];
int cache[MAX_N][MAX_N];
int countCache[MAX_N][MAX_N];

int path(int n, int x, int y)
{
    int &ret = cache[y][x];

    if (y == (n - 1))
    {
        return triangle[y][x];
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = max(path(n, x, y + 1), path(n, x + 1, y + 1)) + triangle[y][x];
    return ret;
}

int count(int n, int x, int y)
{
    int &ret = countCache[y][x];

    if (y == (n - 1))
    {
        return 1;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = 0;
    if (path(n, x + 1, y + 1) >= path(n, x, y + 1))
    {
        ret += count(n, x + 1, y + 1);
    }
    if (path(n, x + 1, y + 1) <= path(n, x, y + 1))
    {
        ret += count(n, x, y + 1);
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;

        memset(&(triangle[0][0]), 0, sizeof(int) * MAX_N * MAX_N);
        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);
        memset(&(countCache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        cin >> n;

        for (int j = 1; j <= n; j++)
        {
            for (int k = 0; k < j; k++)
            {
                cin >> triangle[(j - 1)][k];
            }
        }

        cout << count(n, 0, 0) << endl;
    }

    return 0;
}
