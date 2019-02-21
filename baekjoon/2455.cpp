/*
    2455 : 지능형 기차
    URL : https://www.acmicpc.net/problem/2455
    Input :
        0 32
        3 13
        28 25
        39 0
    Output :
        42
*/

#include <iostream>

int main(int argc, char const *argv[])
{
    int count = 0;
    int countMax = 0;

    for (int i = 0; i < 4; i++)
    {
        int out;
        int in;

        std::cin >> out;
        std::cin >> in;

        count -= out;
        count += in;

        if (count > countMax)
        {
            countMax = count;
        }
    }

    std::cout << countMax;

    return 0;
}
