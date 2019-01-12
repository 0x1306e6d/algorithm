/*
    TRIANGLEPATH : 삼각형 위의 최대 경로
    Difficulty : 하
    Input :
        2
        5
        6
        1 2
        3 7 4
        9 4 1 7
        2 7 5 9 4
        5
        1 
        2 4
        8 16 8
        32 64 32 64
        128 256 128 256 128
    Output :
        28
        341
*/
#include <iostream>
#include <cstring>

#define MAX_N 101

using namespace std;

int triangle[MAX_N][MAX_N];
int cache[MAX_N][MAX_N];

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

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;

        memset(&(triangle[0][0]), 0, sizeof(int) * MAX_N * MAX_N);
        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        cin >> n;

        for (int j = 1; j <= n; j++)
        {
            for (int k = 0; k < j; k++)
            {
                int number;

                cin >> number;

                triangle[(j - 1)][k] = number;
            }
        }

        cout << path(n, 0, 0) << endl;
    }

    return 0;
}
