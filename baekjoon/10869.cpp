/*
    10869 : 사칙연산
    URL : https://www.acmicpc.net/problem/10869
    Input :
        7 3
    Output :
        10
        4
        21
        2
        1
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int A;
    int B;

    cin >> A;
    cin >> B;

    cout << (A + B) << endl;
    cout << (A - B) << endl;
    cout << (A * B) << endl;
    cout << (A / B) << endl;
    cout << (A % B);

    return 0;
}
