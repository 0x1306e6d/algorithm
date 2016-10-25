/*
    10253 : 헨리
    URL : https://www.acmicpc.net/problem/10253
    Input :
        3
        4 23
        5 7
        8 11
    Output :
        138
        70
        4070
*/
#include <iostream>

using namespace std;

int find_henry(int p, int q);

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int a, b;
        cin >> a >> b;
        cout << find_henry(a, b) << endl;
    }
    return 0;
}

int find_henry(int p, int q)
{
    while(p > 1)
    {
        if (q % p == 0)
        {
            q = q / p;
            p = p / p;
            if (p == 1)
            {
                return q;
            }
        }
        int x = (q / p) + 1;
        p = p * x - q;
        q = q * x;
    }
    return q;
}