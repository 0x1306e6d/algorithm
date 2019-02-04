/*
    2749 : 피보나치 수 3
    URL : https://www.acmicpc.net/problem/2749
    Input :
        1000
    Output :
        228875
*/

#include <iostream>
#include <cmath>
#include <cstdint>

#define MOD 1000000
#define PISANO 1500000

using namespace std;

uint64_t n;
uint64_t fibonacci[PISANO + 1];

int main(int argc, char const *argv[])
{
    fibonacci[0] = 0;
    fibonacci[1] = 1;
    for (int i = 2; i <= PISANO; i++)
    {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        fibonacci[i] %= MOD;
    }

    cin >> n;
    cout << fibonacci[n % PISANO];

    return 0;
}
