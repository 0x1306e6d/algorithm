/*
    15552 : 빠른 A+B
    URL : https://www.acmicpc.net/problem/15552
    Input :
        5
        1 1
        12 34
        5 500
        40 60
        1000 1000
    Output :
        2
        46
        505
        100
        2000
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;

    cin.tie(NULL);
    cin.sync_with_stdio(false);

    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int A;
        int B;

        cin >> A;
        cin >> B;

        cout << (A + B) << '\n';
    }

    return 0;
}
