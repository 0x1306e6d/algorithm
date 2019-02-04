/*
    6064 : 카잉 달력
    URL : https://www.acmicpc.net/problem/6064
    Input :
        3
        10 12 3 9
        10 12 7 2
        13 11 5 6
    Output :
        33
        -1
        83
*/

#include <iostream>

using namespace std;

int mkgcd(int a, int b)
{
    if ((a % b) == 0)
    {
        return b;
    }
    else
    {
        return mkgcd(b, a % b);
    }
}

int mklcm(int a, int b)
{
    return (a * b) / mkgcd(a, b);
}

int main(int argc, char const *argv[])
{
    int T;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int M;
        int N;
        int x;
        int y;

        cin >> M;
        cin >> N;
        cin >> x;
        cin >> y;

        int lcm = mklcm(M, N);
        while ((x != y) && (x <= lcm))
        {
            if (x < y)
            {
                x += M;
            }
            else
            {
                y += N;
            }
        }

        if (x != y)
        {
            printf("-1\n");
        }
        else
        {
            printf("%d\n", x);
        }
    }

    return 0;
}
