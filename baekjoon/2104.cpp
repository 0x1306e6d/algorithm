/*
    2104 : 부분배열 고르기
    URL : https://www.acmicpc.net/problem/2104
    Input :
        6
        3 1 6 4 5 2
    Output :
        60
*/

#include <iostream>
#include <cstdint>

int main(int argc, char const *argv[])
{
    std::ios::sync_with_stdio(false);

    int n;
    std::cin >> n;

    int a[n];
    std::pair<uint64_t, int> b[n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> a[i];

        if (i == 0)
        {
            b[i].first = a[i];
            b[i].second = a[i];
        }
        else
        {
            uint64_t x = (b[i - 1].first + a[i]) * (std::min(b[i - 1].second, a[i]));
            uint64_t y = a[i] * a[i];

            if (x > y)
            {
                b[i].first = b[i - 1].first + a[i];
                b[i].second = std::min(b[i - 1].second, a[i]);
            }
            else
            {
                b[i].first = a[i];
                b[i].second = a[i];
            }
        }
    }

    uint64_t answer = 0;
    for (int i = 0; i < n; i++)
    {
        answer = std::max(answer, (b[i].first * b[i].second));
    }
    std::cout << answer;

    return 0;
}
