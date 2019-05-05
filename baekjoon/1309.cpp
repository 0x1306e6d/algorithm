/*
    1309 : 동물원
    URL : https://www.acmicpc.net/problem/1309
    Input :
        4
    Output :
        41
*/

#include <iostream>

#define MAX_N 100001
#define MOD 9901

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    int xx = 1;
    int xo = 1;
    int ox = 1;
    for (int i = 1; i < n; i++)
    {
        int xx2 = (xx + xo + ox) % MOD;
        int xo2 = (xx + ox) % MOD;
        int ox2 = (xx + xo) % MOD;

        xx = xx2;
        xo = xo2;
        ox = ox2;
    }

    std::cout << (xx + xo + ox) % MOD;

    return 0;
}
