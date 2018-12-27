/*
    1009 : 분산처리
    URL : https://www.acmicpc.net/problem/1009
    Input :
        5
        1 6
        3 7
        6 2
        7 100
        9 635
    Output :
        1
        7
        6
        1
        9
*/
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int a;
        int b;
        int p;

        cin >> a;
        cin >> b;

        b = b % 4;
        if (b == 0)
        {
            b = 4;
        }

        p = (int)(pow((a % 10), b));
        p = p % 10;

        if (p == 0)
        {
            cout << 10 << endl;
        }
        else
        {
            cout << p << endl;
        }
    }

    return 0;
}
