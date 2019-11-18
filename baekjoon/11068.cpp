/*
    11068 : 회문인 수
    URL : https://www.acmicpc.net/problem/11068
    Input :
        3
        747
        255
        946734
    Output :
        1
        1
        0
*/

#include <iostream>
#include <vector>

bool isPalindromic(const int BASE, const int NUM);

int main()
{
    int T;
    std::cin >> T;
    while (T--)
    {
        bool palindromic = false;
        int NUM;
        std::cin >> NUM;
        for (int i = 2; i <= 64; ++i)
        {
            if (isPalindromic(i, NUM))
            {
                palindromic = true;
                break;
            }
        }
        if (!palindromic)
        {
            for (int i = 2; i < 10; ++i)
            {
                if (isPalindromic(i, NUM))
                {
                    palindromic = true;
                    break;
                }
            }
        }
        if (palindromic)
        {
            std::cout << 1 << std::endl;            
        }
        else
        {
            std::cout << 0 << std::endl;
        }
    }
    return 0;
}

bool isPalindromic(const int BASE, const int NUM)
{
    int value = NUM;
    std::vector<int> bases;

    while (value)
    {
        bases.push_back(value % BASE);
        value = value / BASE;
    }

    for (int i = 0; i < bases.size(); ++i)
    {
        if (bases[i] != bases[bases.size() - 1 - i])
        {
            return false;
        }
    }
    return true;
}