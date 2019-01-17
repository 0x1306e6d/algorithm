/*
    1110 : 더하기 사이클
    URL : https://www.acmicpc.net/problem/1110
    Input #1 :
        26
    Output #1 :
        4
    Input #2 :
        55
    Output #2 :
        3
    Input #3 :
        1
    Output #3 :
        60
*/
#include <iostream>

using namespace std;

int N;

int make(int n)
{
    int m = (n / 10) + (n % 10);
    return ((n % 10) * 10) + (m % 10);
}

int cycle(int n)
{
    if (n == N)
    {
        return 1;
    }
    else
    {
        return 1 + cycle(make(n));
    }
}

int main(int argc, char const *argv[])
{
    cin >> N;
    cout << cycle(make(N));

    return 0;
}
