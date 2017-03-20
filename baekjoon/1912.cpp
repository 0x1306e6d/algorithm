/*
    1912 : 연속합
    URL : https://www.acmicpc.net/problem/1912
    Input : 
        10
        10 -4 3 1 5 6 -35 12 21 -1
    Output :
        33
*/
#include <iostream>
#include <stdio.h>
#include <limits.h>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int array[N];
    int sum[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i];
    }

    sum[0] = array[0];
    int largest = sum[0];
    for (int i = 1; i < N; i++)
    {
        sum[i] = array[i];
        if (sum[i - 1] > 0)
        {
            sum[i] = sum[i - 1] + sum[i];
        }

        if (sum[i] > largest)
        {
            largest = sum[i];
        }
    }
    cout << largest;

    return 0;
}