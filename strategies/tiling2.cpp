/*
    TILING2 : 타일링
    Difficulty : 하
    Input :
        3
        1
        5
        100
    Output :
        1
        8
        782204094
*/
#include <iostream>
#include <cstring>

#define MAX_N 101
#define MOD 1000000007

using namespace std;

int cache[MAX_N];

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

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;

        memset(&(cache[0]), -1, sizeof(int) * MAX_N);

        cin >> n;

        cout << tiling(n) << endl;
    }

    return 0;
}
