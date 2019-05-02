/*
    1016 : 제곱 ㄴㄴ 수
    URL : https://www.acmicpc.net/problem/1016
    Input :
        1 10
    Output :
        7
*/

#include <iostream>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <vector>

#define MAX_N 1000001

bool sieve[MAX_N];

void eratosthenes(int n)
{
    sieve[0] = false;
    sieve[1] = false;

    int sqrtn = int(std::sqrt(n));
    for (int i = 2; i <= sqrtn; i++)
    {
        if (sieve[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                sieve[j] = false;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    std::vector<uint64_t> primes;

    uint64_t min;
    uint64_t max;
    std::cin >> min;
    std::cin >> max;

    memset(&(sieve[0]), true, sizeof(bool) * MAX_N);

    uint64_t s = uint64_t(std::sqrt(max));
    eratosthenes(s);
    for (uint64_t i = 0; i <= s; i++)
    {
        if (sieve[i])
        {
            primes.push_back(i);
        }
    }

    memset(&(sieve[0]), true, sizeof(bool) * MAX_N);

    uint64_t count = (max - min + 1);
    for (std::vector<uint64_t>::iterator it = primes.begin();
         it != primes.end();
         ++it)
    {
        uint64_t prime = *it;
        uint64_t expp = prime * prime;
        uint64_t first = min;
        if ((min % expp) != 0)
        {
            first = (min + expp) - (min % expp);
        }

        for (uint64_t i = first; i <= max; i += expp)
        {
            uint64_t index = i - min;
            if (sieve[index])
            {
                sieve[index] = false;
                count--;
            }
        }
    }

    std::cout << count;

    return 0;
}
