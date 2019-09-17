/*
    1049 : 기타줄
    URL : https://www.acmicpc.net/problem/1049
    Input :
        4 2
        12 3
        15 4
    Output :
        12
*/

#include <iostream>

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    int minSix = 1004;
    int minOne = 1004;

    for (int i = 0; i < m; i++)
    {
        int six;
        int one;
        std::cin >> six;
        std::cin >> one;

        minSix = std::min(minSix, six);
        minOne = std::min(minOne, one);
    }

    int sixCount = (n / 6);
    int mixSixAndOne = (minSix * sixCount) + (minOne * (n - (6 * sixCount)));
    int onlySix = (minSix * (sixCount + 1));
    int onlyOne = (minOne * n);
    std::cout << std::min(mixSixAndOne, std::min(onlySix, onlyOne));

    return 0;
}
