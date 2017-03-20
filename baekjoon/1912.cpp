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

    int sum = INT_MIN;
    int largest = INT_MIN;
    while (N--)
    {
        int i;
        cin >> i;

        if (sum == INT_MIN)
        {
            sum = i;
        }
        else
        {
            if (sum > 0)
            {
                sum = sum + i;
            }
            else
            {
                sum = i;
            }
        }

        if (sum > largest)
        {
            largest = sum;
        }
    }
    cout << largest;
    return 0;
}