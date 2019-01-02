/*
    10430 : 나머지
    URL : https://www.acmicpc.net/problem/10430
    Input :
        5 8 4
    Output :
        1
        1
        0
        0
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int A;
    int B;
    int C;

    cin >> A;
    cin >> B;
    cin >> C;

    cout << ((A + B) % C) << endl;
    cout << ((A % C + B % C) % C) << endl;
    cout << ((A * B) % C) << endl;
    cout << ((A % C * B % C) % C);

    return 0;
}
