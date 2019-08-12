/*
    2869 : 달팽이는 올라가고 싶다
    URL : https://www.acmicpc.net/problem/2869
    Input :
        2 1 5
    Output :
        4
*/

#include <iostream>
#include <cmath>

int main(int argc, char const *argv[])
{
    int a;
    int b;
    int v;
    std::cin >> a;
    std::cin >> b;
    std::cin >> v;

    int velocity = a - b;
    int left = std::ceil((double)v / (double)a);
    int right = std::ceil((double)v / (double)velocity);
    while (left <= right)
    {
        int mid = (left + right) / 2;

        if (((a * mid) - (b * (mid - 1))) >= v)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    std::cout << left;

    return 0;
}
