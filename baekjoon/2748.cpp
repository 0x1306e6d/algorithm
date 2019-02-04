/*
    2748 : 피보나치 수 2
    URL : https://www.acmicpc.net/problem/2748
    Input :
        10
    Output :
        55
*/

#include <iostream>
#include <cstdint>
#include <cstring>

#define MAX_N 91

using namespace std;

uint64_t CACHE[MAX_N];

uint64_t fibonacci(int n)
{
    uint64_t &ret = CACHE[n];

    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = fibonacci(n - 1) + fibonacci(n - 2);
    return ret;
}

int main(int argc, char const *argv[])
{
    int n;

    memset(&(CACHE[0]), -1, sizeof(uint64_t) * MAX_N);

    cin >> n;
    cout << fibonacci(n);

    return 0;
}
