/*
    1004 : 어린 왕자
    URL : https://www.acmicpc.net/problem/1004
    Input :
        2
        -5 1 12 1
        7
        1 1 8
        -3 -1 1
        2 2 2
        5 5 1
        -4 5 1
        12 1 1
        12 1 2
        -5 1 5 1
        1
        0 0 2
    Output :
        3
        0
*/
#include <iostream>
#include <math.h>

using namespace std;

bool is_in(int x, int y, int a, int b, int r)
{
    if (pow(x - a, 2) + pow(y - b, 2) - pow(r, 2) < 0)
    {
        return true;
    }
    return false;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int count = 0;
        int x1, y1;
        int x2, y2;
        int n;
        cin >> x1 >> y1;
        cin >> x2 >> y2;
        cin >> n;

        while (n--)
        {
            int cx, cy;
            int r;
            cin >> cx >> cy;
            cin >> r;

            bool is_src_in = is_in(x1, y1, cx, cy, r);
            bool is_dstn_in = is_in(x2, y2, cx, cy, r);

            if ((is_src_in && !is_dstn_in) || (!is_src_in && is_dstn_in))
            {
                count++;
            }
        }

        cout << count << endl;
    }
    return 0;
}