/*
    1012 : 유기농 배추
    URL : https://www.acmicpc.net/problem/1012
    Input :
        2
        10 8 17
        0 0
        1 0
        1 1
        4 2
        4 3
        4 5
        2 4
        3 4
        7 4
        8 4
        9 4
        7 5
        8 5
        9 5
        7 6
        8 6
        9 6
        10 10 1
        5 5
    Output :
        5
        1
*/

#include <iostream>
#include <cstring>

#define MAX_M 51
#define MAX_N 51

using namespace std;

int M;
int N;

bool field[MAX_M][MAX_N];
bool visited[MAX_M][MAX_N];

bool find(int x, int y)
{
    if (field[x][y] == false)
    {
        return false;
    }
    if (visited[x][y])
    {
        return false;
    }

    visited[x][y] = true;
    if (x > 0)
    {
        find(x - 1, y);
    }
    if (y > 0)
    {
        find(x, y - 1);
    }
    if ((x + 1) < M)
    {
        find(x + 1, y);
    }
    if ((y + 1) < N)
    {
        find(x, y + 1);
    }
    return true;
}

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int K;

        memset(&(field[0][0]), false, sizeof(bool) * MAX_M * MAX_N);
        memset(&(visited[0][0]), false, sizeof(bool) * MAX_M * MAX_N);

        cin >> M;
        cin >> N;
        cin >> K;

        for (int j = 0; j < K; j++)
        {
            int x;
            int y;

            cin >> x;
            cin >> y;

            field[x][y] = true;
        }

        int count = 0;
        for (int x = 0; x < M; x++)
        {
            for (int y = 0; y < N; y++)
            {
                if (find(x, y))
                {
                    count += 1;
                }
            }
        }

        cout << count << endl;
    }

    return 0;
}
