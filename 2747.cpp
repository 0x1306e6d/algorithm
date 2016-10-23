/*
    2747 : 피보나치 수
    URL : https://www.acmicpc.net/problem/2747
    Input :
        10
    Output :
        55
*/
#include <iostream>
#include <string.h>

#define MAX 45
using namespace std;

int STORE[MAX];

int fibonacci(int n);

int main()
{
    memset(STORE, 0, sizeof(STORE));

    int n;
    cin >> n;
    cout << fibonacci(n);
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