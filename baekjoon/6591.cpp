/*
    6591 : 이항 쇼다운
    URL : https://www.acmicpc.net/problem/6591
    Input :
        4 2
        10 5
        49 6
        0 0
    Output :
        6
        252
        13983816
*/

#include <iostream>
#include <cstdint>

uint64_t binomial(int n, int k)
{
    uint64_t result = 1;
    for (int i = 1; i <= k; i++)
    {
        result = (result * (n--)) / i;
    }
    return result;
}

int main(int argc, char const *argv[])
{
    int n;
    int k;

    while (true)
    {
        std::cin >> n;
        std::cin >> k;
        if ((n == 0) && (k == 0))
        {
            break;
        }

        std::cout << binomial(n, std::min(k, n - k)) << std::endl;
    }

    return 0;
}
