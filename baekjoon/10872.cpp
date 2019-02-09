/*
    10872 : 팩토리얼
    URL : https://www.acmicpc.net/problem/10872
    Input :
        10
    Output :
        3628800
*/

#include <iostream>
#include <cstdint>

using namespace std;

uint64_t factorial(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }

    return n * factorial(n - 1);
}

int main(int argc, char const *argv[])
{
    int N;

    cin >> N;
    cout << factorial(N);

    return 0;
}
