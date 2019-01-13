/*
    POLY : 폴리오미노
    Difficulty : 중
    Input :
        3
        2
        4
        92
    Output :
        2
        19
        4841817
*/
#include <iostream>
#include <cstring>

#define MAX_N 101
#define MOD 10000000

using namespace std;

int cache[MAX_N][MAX_N];

int poly(int n, int first)
{
    int &ret = cache[n][first];

    if (n == first)
    {
        return 1;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = 0;
    for (int second = 1; second <= (n - first); second++)
    {
        int add = first + second - 1;
        add *= poly(n - first, second);
        add %= MOD;

        ret += add;
        ret %= MOD;
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
        int count = 0;

        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        cin >> n;

        for (int j = 1; j <= n; j++)
        {
            count += poly(n, j);
        }

        cout << (count % MOD) << endl;
    }

    return 0;
}
