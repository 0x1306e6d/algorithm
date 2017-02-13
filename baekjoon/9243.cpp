/*
    9243 : 파일 완전 삭제
    URL : https://www.acmicpc.net/problem/9243
    Input #1 :
        1
        10001110101000001111010100001110
        01110001010111110000101011110001
    Output #1 :
        Deletion succeeded
    Input #2 :
        20
        0001100011001010
        0001000011000100
    Output #2 :
        Deletion failed
*/
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    string before;
    string after;
    cin >> N;
    cin >> before;
    cin >> after;

    if (N % 2 == 0)
    {
        for (int i = 0; i < before.size(); i++)
        {
            if (before.at(i) != after.at(i))
            {
                cout << "Deletion failed";
                return 0;
            }
        }
        cout << "Deletion succeeded";
    }
    else
    {
        for (int i = 0; i < before.size(); i++)
        {
            if (before.at(i) == after.at(i))
            {
                cout << "Deletion failed";
                return 0;
            }
        }
        cout << "Deletion succeeded";
    }
    return 0;
}