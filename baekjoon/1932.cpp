/*
    1932 : 정수 삼각형
    URL : https://www.acmicpc.net/problem/1932
    Input :
        5
        7
        3 8
        8 1 0
        2 7 4 4
        4 5 2 6 5
    Output :
        30
*/

#include <iostream>
#include <cstring>

#define MAX_N 501

using namespace std;

int N;

int triangle[MAX_N][MAX_N];

int main(int argc, char const *argv[])
{
    cin >> N;

    memset(&(triangle[0][0]), 0, sizeof(int) * MAX_N * MAX_N);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cin >> triangle[i][j];
        }
    }

    for (int i = 1; i < N; i++)
    {
        triangle[i][0] += triangle[i - 1][0];
        for (int j = 1; j <= (i - 1); j++)
        {
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j]);
        }
        triangle[i][i] += triangle[i - 1][i - 1];
    }

    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum = max(sum, triangle[N - 1][i]);
    }
    cout << sum;

    return 0;
}
