/*
    10870 : 피보나치 수 5
    URL : https://www.acmicpc.net/problem/10870
    Input :
        10
    Output :
        55
*/

#include <iostream>

int fibonacci(int n)
{
    if (n == 2)
    {
        return 1;
    }
    if (n == 1)
    {
        return 1;
    }
    if (n == 0)
    {
        return 0;
    }

    return (fibonacci(n - 1) + fibonacci(n - 2));
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::cout << fibonacci(n);

    return 0;
}
