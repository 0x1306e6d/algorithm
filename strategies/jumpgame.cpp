/*
    JUMPGAME : 외발 뛰기
    Difficulty : 하
    Input :
        2
        7
        2 5 1 6 1 4 1
        6 1 1 2 2 9 3
        7 2 3 2 1 3 1
        1 1 3 1 7 1 2
        4 1 2 3 4 1 2
        3 3 1 2 3 4 1
        1 5 2 9 4 7 0
        7
        2 5 1 6 1 4 1
        6 1 1 2 2 9 3
        7 2 3 2 1 3 1
        1 1 3 1 7 1 2
        4 1 2 3 4 1 3
        3 3 1 2 3 4 1
        1 5 2 9 4 7 0 
    Output :
        YES
        NO
*/
#include <iostream>

#define MAX_N 101

using namespace std;

int matrix[MAX_N][MAX_N];
int cache[MAX_N][MAX_N];

int jump(int x, int y, int n)
{
    if ((x == (n - 1)) && (y == (n - 1)))
    {
        return 1;
    }
    else if ((x >= n) || (y >= n))
    {
        return 0;
    }

    int &ret = cache[x][y];
    if (ret == -1)
    {
        ret = jump(x + matrix[x][y], y, n) || jump(x, y + matrix[x][y], n);
        return ret;
    }
    else
    {
        return ret;
    }
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;

        cin >> n;

        memset(&(matrix[0][0]), 0, sizeof(int) * MAX_N * MAX_N);
        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                int size;

                cin >> size;

                matrix[j][k] = size;
            }
        }

        if (jump(0, 0, n))
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }
    }

    return 0;
}
