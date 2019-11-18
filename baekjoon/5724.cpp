/*
    5724 : 파인만
    URL : https://www.acmicpc.net/problem/5724
    Input :
        2
        1
        8
        0
    Output :
        5
        1
        204
*/

#include <iostream>

using namespace std;

int main()
{
    while (true)
    {
        int N;
        cin >> N;
        if (N == 0)
        {
            break;
        }
        else
        {
            int sum = 0;
            for (int i = 1; i <= N; i++)
            {
                sum += (i * i);
            }
            cout << sum << endl;
        }
    }
    return 0;
}