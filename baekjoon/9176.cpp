/*
    9176: 메르센 합성수
    URL: https://www.acmicpc.net/problem/9176
    Input:
        31
    Output:
        23 * 89 = 2047 = ( 2 ^ 11 ) - 1
        47 * 178481 = 8388607 = ( 2 ^ 23 ) - 1
        233 * 1103 * 2089 = 536870911 = ( 2 ^ 29 ) - 1
*/

#include <iostream>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <vector>

#define MAX_K 64

bool sieve[MAX_K];

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

bool isPrime(uint64_t n)
{
    if (n < 63)
    {
        return sieve[n];
    }

    if ((n % 2) == 0)
    {
        return true;
    }

    if ((n % 3) == 0)
    {
        return true;
    }

    int i = 5;
    int sqrtn = int(std::sqrt(n));
    while (i <= sqrtn)
    {
        if (((n % i) == 0) || ((n % (i + 2)) == 0))
        {
            return false;
        }

        i += 6;
    }

    return true;
}

std::vector<uint64_t> factorize(uint64_t n)
{
    std::vector<uint64_t> factors;

    uint64_t i = 2;
    uint64_t sqrtn = uint64_t(std::sqrt(n));
    while ((n > 1) && (i <= sqrtn))
    {
        while ((n % i) == 0)
        {
            n = (n / i);
            sqrtn = uint64_t(std::sqrt(n));
            factors.push_back(i);
        }

        i++;
    }

    if (n > 1)
    {
        factors.push_back(n);
    }

    return factors;
}

int main(int argc, char const *argv[])
{
    std::memset(&(sieve[0]), true, sizeof(bool) * MAX_K);

    eratosthenes(63);

    int k;
    scanf("%d", &k);

    for (int p = 0; p <= std::min(59, k); p++)
    {
        if (sieve[p])
        {
            uint64_t m = uint64_t(std::pow(2, p)) - 1;

            if (!isPrime(m))
            {
                std::vector<uint64_t> factors = factorize(m);

                for (int i = 0; i < factors.size(); i++)
                {
                    printf("%llu", factors[i]);

                    if (i < (factors.size() - 1))
                    {
                        printf(" * ");
                    }
                }
                printf(" = %llu = ( 2 ^ %d ) - 1\n", m, p);
            }
        }
    }

    return 0;
}
