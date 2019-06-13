/*
    2798 : 블랙잭
    URL : https://www.acmicpc.net/problem/2798
    Input :
        5 21
        5 6 7 8 9
    Output :
        21
*/

#include <iostream>
#include <algorithm>

#define MAX_N 101

int cards[MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < n; i++)
    {
        std::cin >> cards[i];
    }

    std::sort(&(cards[0]), &(cards[n]));

    int sum = 0;
    for (int i = (n - 1); i >= 0; i--)
    {
        for (int j = (i - 1); j >= 0; j--)
        {
            for (int k = (j - 1); k >= 0; k--)
            {
                int s = (cards[i] + cards[j] + cards[k]);
                if (s > m)
                {
                    continue;
                }
                sum = std::max(sum, s);
            }
        }
    }

    std::cout << sum;

    return 0;
}
