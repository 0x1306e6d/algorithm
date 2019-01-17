/*
    11726 : 2×n 타일링
    URL : https://www.acmicpc.net/problem/11726
    Input #1 :
        2
    Output #1 :
        2
    Input #2 :
        9
    Output #2 :
        55
*/
#include <iostream>
#include <cstring>

#define MAX_N 1001
#define MOD 10007

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
    int n;

    memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    cin >> n;
    cout << tiling(n);

    return 0;
}
