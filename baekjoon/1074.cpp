/*
    1074 : Z
    URL : https://www.acmicpc.net/problem/1074
    Input #1 :
        2 3 1
    Output #1 :
        11
    Input #2 :
        3 7 7
    Output #2 :
        63
*/

#include <iostream>
#include <cmath>
#include <cstdint>

uint64_t Z(int n, int r, int c)
{
    if (n == 1)
    {
        if ((r % 2) == 0)
        {
            if ((c % 2) == 0)
            {
                return 1;
            }
            else
            {
                return 2;
            }
        }
        else
        {
            if ((c % 2) == 0)
            {
                return 3;
            }
            else
            {
                return 4;
            }
        }
    }

    int mid = (int)std::pow(2, n - 1);
    if ((r < mid) && (c < mid))
    {
        return Z(n - 1, r, c);
    }
    if ((r < mid) && (c >= mid))
    {
        return (uint64_t)std::pow(mid, 2) + Z(n - 1, r, c - mid);
    }
    if ((r >= mid) && (c < mid))
    {
        return ((uint64_t)std::pow(mid, 2) * 2) + Z(n - 1, r - mid, c);
    }
    if ((r >= mid) && (c >= mid))
    {
        return ((uint64_t)std::pow(mid, 2) * 3) + Z(n - 1, r - mid, c - mid);
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    int n;
    int r;
    int c;
    std::cin >> n;
    std::cin >> r;
    std::cin >> c;

    std::cout << (Z(n, r, c) - 1);

    return 0;
}
