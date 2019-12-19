/*
    1159 : 농구 경기
    URL : https://www.acmicpc.net/problem/1159
    Input :
        18
        babic
        keksic
        boric
        bukic
        sarmic
        balic
        kruzic
        hrenovkic
        beslic
        boksic
        krafnic
        pecivic
        klavirkovic
        kukumaric
        sunkic
        kolacic
        kovacic
        prijestolonasljednikovi
    Output :
        bk
*/

#include <iostream>

int counts[26];

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::string s;
        std::cin >> s;

        counts[(s.at(0) - 'a')] += 1;
    }

    bool flag = false;
    for (int i = 0; i < 26; i++)
    {
        if (counts[i] >= 5)
        {
            std::cout << (char)('a' + i);

            flag = true;
        }
    }

    if (!flag)
    {
        std::cout << "PREDAJA";
    }

    return 0;
}
