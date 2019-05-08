/*
    14562 : 태권왕
    URL : https://www.acmicpc.net/problem/14562
    Input :
        6
        10 20
        2 7
        15 62
        10 37
        11 50
        34 59
    Output :
        3
        3
        4
        4
        5
        25
*/

#include <iostream>

int balchagi(int s, int t)
{
    if (s == t)
    {
        return 0;
    }

    int ret = 0;
    if ((s + 1) <= t)
    {
        ret = (1 + balchagi(s + 1, t));
    }
    if ((s + s) <= (t + 3))
    {
        ret = std::min(ret, 1 + balchagi(s + s, t + 3));
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        int s;
        int t;
        std::cin >> s;
        std::cin >> t;

        std::cout << balchagi(s, t) << std::endl;
    }

    return 0;
}
