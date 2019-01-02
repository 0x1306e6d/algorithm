/*
    10952 : A+B - 5
    URL : https://www.acmicpc.net/problem/10952
    Input :
        1 1
        2 3
        3 4
        9 8
        5 2
        0 0
    Output :
        2
        5
        7
        17
        7
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int A;
    int B;

    while (true)
    {
        cin >> A;
        cin >> B;

        if ((A == 0) && (B == 0))
        {
            break;
        }

        cout << (A + B) << endl;
    }

    return 0;
}
