/*
    2775 : 부녀회장이 될테야
    URL : https://www.acmicpc.net/problem/2775
    Input :
        2
        1
        3
        2
        3
    Output :
        6
        10
*/

#include <iostream>

#define MAX_K 15
#define MAX_N 15

using namespace std;

int main(int argc, char const *argv[])
{
    int homes[MAX_K][MAX_N];

    int T;
    cin >> T;

    for (int n = 1; n < MAX_N; n++)
    {
        homes[0][n] = n;
    }

    for (int k = 1; k < MAX_K; k++)
    {
        for (int n = 1; n < MAX_N; n++)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += homes[k - 1][i];
            }
            homes[k][n] = sum;
        }
    }

    for (int i = 0; i < T; i++)
    {
        int k;
        int n;
        cin >> k;
        cin >> n;

        cout << homes[k][n] << endl;
    }

    return 0;
}
