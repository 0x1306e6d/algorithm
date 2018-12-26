/*
    1002 : 터렛
    URL : https://www.acmicpc.net/problem/1002
    Input :
        3
        0 0 13 40 0 37
        0 0 3 0 7 4
        1 1 1 1 1 5
    Output :
        2
        1
        0
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
        int x1;
        int y1;
        int r1;
        int x2;
        int y2;
        int r2;
        double d;

        cin >> x1;
        cin >> y1;
        cin >> r1;
        cin >> x2;
        cin >> y2;
        cin >> r2;

        if ((x1 == x2) && (y1 == y2))
        {
            if (r1 == r2)
            {
                cout << -1 << endl;
            }
            else
            {
                cout << 0 << endl;
            }
        }
        else
        {
            d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
            if ((d < (r1 + r2) && d > abs(r1 - r2)))
            {
                cout << 2 << endl;
            }
            else if ((d == (r1 + r2)) || (d == abs(r1 - r2)))
            {
                cout << 1 << endl;
            }
            else
            {
                cout << 0 << endl;
            }
        }
    }

    return 0;
}
