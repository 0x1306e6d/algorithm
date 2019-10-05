/*
    1629: 곱셈
    URL: https://www.acmicpc.net/problem/1629
    Input #1:
        10 11 12
    Output #1:
        4
*/

#include <iostream>
#include <cstdint>

uint64_t pow(uint64_t a, uint64_t b, uint64_t c)
{
    if (b == 0)
    {
        return 1;
    }

    uint64_t n = pow(a, b / 2, c);
    uint64_t m = (n * n) % c;
    if ((b % 2) == 0)
    {
        return m;
    }
    else
    {
        return (m * a) % c;
    }
}

int main(int argc, char const *argv[])
{
    uint64_t a;
    uint64_t b;
    uint64_t c;

    std::cin >> a;
    std::cin >> b;
    std::cin >> c;

    std::cout << pow(a, b, c);

    return 0;
}
