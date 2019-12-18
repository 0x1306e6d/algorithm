/*
    15719 : 중복된 숫자
    URL : https://www.acmicpc.net/problem/15719
    Input :
        10
        1 2 2 5 6 4 3 7 8 9
    Output :
        2
*/

#include <iostream>

#define MAX_N 10000001

bool a[MAX_N];

int main(int argc, char const *argv[])
{
    std::ios::sync_with_stdio(false);

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        int j;
        std::cin >> j;

        if (a[j])
        {
            std::cout << j;
            break;
        }
        else
        {
            a[j] = true;
        }
    }

    return 0;
}
