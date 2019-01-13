/*
    NUMB3RS : 두니발 박사의 탈옥
    Difficulty : 중
    Input :
        2
        5 2 0
        0 1 1 1 0
        1 0 0 0 1
        1 0 0 0 0
        1 0 0 0 0
        0 1 0 0 0
        3
        0 2 4
        8 2 3
        0 1 1 1 0 0 0 0
        1 0 0 1 0 0 0 0
        1 0 0 1 0 0 0 0
        1 1 1 0 1 1 0 0
        0 0 0 1 0 0 1 1
        0 0 0 1 0 0 0 1
        0 0 0 0 1 0 0 0
        0 0 0 0 1 1 0 0
        4
        3 1 2 6
    Output :
        0.83333333 0.00000000 0.16666667
        0.43333333 0.06666667 0.06666667 0.06666667
*/
#include <iostream>
#include <cstring>

#define MAX_N 51
#define MAX_D 101

using namespace std;

int n;
int d;
int p;
int q;

int connected[MAX_N][MAX_N];
int degree[MAX_N];
double cache[MAX_N][MAX_D];

double search1(int here, int days)
{
    double &ret = cache[here][days];

    if (days == d)
    {
        return (here == q) ? 1.0 : 0.0;
    }

    if (ret != -1.0)
    {
        return ret;
    }

    ret = 0.0;
    for (int there = 0; there < n; there++)
    {
        if (connected[here][there])
        {
            ret += search1(there, days + 1) / degree[here];
        }
    }

    return ret;
}

double search2(int here, int days)
{
    double &ret = cache[here][days];

    if (days == 0)
    {
        return (here == p) ? 1.0 : 0.0;
    }

    if (ret != -1.0)
    {
        return ret;
    }

    ret = 0.0;
    for (int there = 0; there < n; there++)
    {
        if (connected[here][there])
        {
            ret += search2(there, days - 1) / degree[there];
        }
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cout.precision(10);
    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int t;

        memset(&(connected[0]), 0, sizeof(int) * MAX_N * MAX_N);
        memset(&(degree[0]), 0, sizeof(int) * MAX_N);

        cin >> n;
        cin >> d;
        cin >> p;

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                cin >> connected[j][k];

                if (connected[j][k] == 1)
                {
                    degree[j] += 1;
                }
            }
        }

        for (int j = 0; j < MAX_N; j++)
        {
            for (int k = 0; k < MAX_D; k++)
            {
                cache[j][k] = -1.0;
            }
        }

        cin >> t;

        for (int j = 0; j < t; j++)
        {
            cin >> q;

            cout << fixed << search2(q, d) << ' ';
        }
        cout << endl;
    }

    return 0;
}
