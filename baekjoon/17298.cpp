/*
    17298: 오큰수
    URL: https://www.acmicpc.net/problem/17298
    Input #1:
        4
        3 5 2 7
    Output #1:
        5 7 7 -1
    Input #2:
        4
        9 5 4 8
    Output #2:
        -1 8 8 -1
*/

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    std::vector<int> nge(n, -1);

    for (int i = 0; i < n; i++)
    {
        std::cin >> a[i];
    }

    for (int i = n - 1; i >= 0; i--)
    {
        int x = a[i];

        for (int j = i - 1; (a[j] < x) && (j >= 0); j--)
        {
            nge[j] = x;
        }
    }

    for (int i = 0; i < n; i++)
    {
        std::cout << nge[i] << ' ';
    }

    return 0;
}