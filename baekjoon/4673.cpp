/*
    4673 : 셀프 넘버
    URL : https://www.acmicpc.net/problem/4673
    Input :
    Output :
        1
        3
        5
        7
        9
        20
        31
        42
        53
        64
        |
        |       <-- a lot more numbers
        |
        9903
        9914
        9925
        9927
        9938
        9949
        9960
        9971
        9982
        9993
*/
#include <iostream>
#include <cstring>

#define MAX_N 10001

using namespace std;

int cache[MAX_N];

void d(int n)
{
    int q = n / 10000;
    int w = (n % 10000) / 1000;
    int e = (n % 1000) / 100;
    int r = (n % 100) / 10;
    int t = n % 10;
    int y = n + q + w + e + r + t;

    if (y < MAX_N)
    {
        cache[y] = 1;
        d(y);
    }
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);

    memset(&(cache[0]), 0, sizeof(int) * MAX_N);

    for (int i = 1; i <= 10000; i++)
    {
        d(i);
    }

    for (int i = 1; i <= 10000; i++)
    {
        if (cache[i] == 0)
        {
            cout << i << '\n';
        }
    }

    return 0;
}
