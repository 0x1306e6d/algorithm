/*
    1003 : 피보나치 함수
    URL : https://www.acmicpc.net/problem/1003
    Input :
        3
        0
        1
        3
    Output :
        1 0
        0 1
        1 2
*/
#include <iostream>
#include <string.h>

#define MAX 40
using namespace std;

int fibonacci(int n);
int STORE[MAX];

int main()
{
    memset(STORE, 0, sizeof(STORE));

    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        if (N == 0)
        {
            cout << "1 0" << endl;
        }
        else if (N == 1)
        {
            cout << "0 1" << endl;
        }
        else
        {
            cout << fibonacci(N - 1) << ' ' << fibonacci(N) << endl;
        }
    }
    return 0;
}

int fibonacci(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        int a = STORE[n - 1];
        if (a == 0)
        {
            a = fibonacci(n - 1);
            STORE[n - 1] = a;
        }
        int b = STORE[n - 2];
        if (b == 0)
        {
            b = fibonacci(n - 2);
            STORE[n - 2] = b;
        }
        return a + b;
    }
}