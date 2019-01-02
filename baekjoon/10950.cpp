/*
    10950 : A+B - 3
    URL : https://www.acmicpc.net/problem/10950
    Input :
        5
        1 1
        2 3
        3 4
        9 8
        5 2
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
    int N;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int A;
        int B;

        cin >> A;
        cin >> B;

        cout << (A + B) << endl;
    }

    return 0;
}
