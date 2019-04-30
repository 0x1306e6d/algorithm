/*
    1977 : 완전제곱수
    URL : https://www.acmicpc.net/problem/1977
    Input #1 :
        60
        100
    Output #1 :
        245
        64
    Input #2 :
        75
        80
    Output #2 :
        -1
*/

#include <iostream>
#include <cmath>

int main(int argc, char const *argv[])
{
    int m;
    int n;
    std::cin >> m;
    std::cin >> n;

    int sum = 0;
    int min = (m == 1) ? 1 : ((int)std::sqrt(m) + 1);
    for (int i = min; (i * i) <= n; i++)
    {
        sum += (i * i);
    }

    if (sum == 0)
    {
        std::cout << -1;
    }
    else
    {
        std::cout << sum << std::endl;
        std::cout << (min * min);
    }

    return 0;
}
