/*
    11399 :  ATM
    URL : https://www.acmicpc.net/problem/11399
    Input :
        5
        3 1 4 3 2
    Output :
        32
*/
#include <iostream>
#include <algorithm>

#define MAX 1000
using namespace std;

int P[MAX];

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        cin >> P[i];
    }

    sort(P, P + N);

    long long sum = 0;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j <= i; ++j)
        {
            sum += P[j];
        }
    }
    cout << sum;
    return 0;
}