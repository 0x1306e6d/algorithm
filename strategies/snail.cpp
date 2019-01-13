/*
    SNAIL : 달팽이
    Difficulty : 하
    Input :
        4
        5 4
        5 3
        4 2
        3 2
    Output :
        0.9960937500
        0.8437500000
        0.5625000000
        0.9375000000
*/
#include <iostream>

#define MAX_N 1001

using namespace std;

double cache[MAX_N][MAX_N];

double climb(int n, int m, int days, int climbed)
{
    double &ret = cache[days][climbed];

    if (days == m)
    {
        return (climbed >= n) ? 1 : 0;
    }

    if (ret != -1.0)
    {
        return ret;
    }

    ret = (0.25 * climb(n, m, days + 1, climbed + 1)) +
          (0.75 * climb(n, m, days + 1, climbed + 2));
    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cout.precision(10);
    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;
        int m;

        for (int j = 0; j < MAX_N; j++)
        {
            for (int k = 0; k < MAX_N; k++)
            {
                cache[j][k] = -1.0;
            }
        }

        cin >> n;
        cin >> m;

        cout << fixed << climb(n, m, 0, 0) << endl;
    }

    return 0;
}
