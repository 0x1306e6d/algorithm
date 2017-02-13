/*
    2839 : 설탕 배달
    URL : https://www.acmicpc.net/problem/2839
    Input :
        18
    Output :
        4
*/
#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int five = (N / 5);
    int three = (N % 5) / 3;

    do
    {
        if ((5 * five) + (3 * three) == N)
        {
            cout << (five + three);
            return 0;
        }
        else
        {
            five = five - 1;
            three = (N - (5 * five)) / 3;
        }
    } while (five >= 0);
    cout << -1;

    return 0;
}