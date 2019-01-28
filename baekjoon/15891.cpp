/*
    15891 : 스타트링크 사무실을 파헤쳐보자
    URL : https://www.acmicpc.net/problem/15552
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int x;

    cin >> x;

    switch (x)
    {
    case 1:
        // 스타트링크 사무실에 있는 가장 큰 TV는 X인치다.
        cout << 65;
        return 0;
    case 2:
        // 스타트링크 사무실 벽에 붙어있는 포스터는 X장이다.
        cout << 17;
        return 0;
    case 3:
        // 스타트링크 사무실 안에 있는 iPad의 개수는 X개이다. (모든 iPad 시리즈 전부 포함)
        cout << 4;
        return 0;
    case 4:
        // 스타트링크 사무실 안에 있는 모니터의 개수는 X개이다.
        cout << 4;
        return 0;
    case 5:
        // 스타트링크 사무실에 있는 게임용 컴퓨터의 RAM의 총 용량은 X GB이다.
        cout << 64;
        return 0;
    default:
        return x;
    }
}