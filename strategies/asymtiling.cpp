/*
    ASYMTILING : 비대칭 타일링
    Difficulty : 하
    Input :
        3
        2
        4
        92
    Output :
        0
        2
        913227494
*/
#include <iostream>
#include <cstring>

#define MAX_N 101
#define MOD 1000000007

using namespace std;

int cache[MAX_N];
int cache2[MAX_N];

int tiling(int width)
{
    int &ret = cache[width];

    if (width <= 1)
    {
        return 1;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = (tiling(width - 1) + tiling(width - 2)) % MOD;
    return ret;
}

int asymmetric(int width)
{
    int &ret = cache2[width];

    if (width <= 2)
    {
        return 0;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = asymmetric(width - 2) % MOD;
    ret = (ret + asymmetric(width - 4)) % MOD;
    ret = (ret + tiling(width - 3)) % MOD;
    ret = (ret + tiling(width - 3)) % MOD;
    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;

        memset(&(cache[0]), -1, sizeof(int) * MAX_N);
        memset(&(cache2[0]), -1, sizeof(int) * MAX_N);

        cin >> n;

        cout << asymmetric(n) << endl;
    }

    return 0;
}
