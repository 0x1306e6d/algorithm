/*
    8320 : 직사각형을 만드는 방법
    URL : https://www.acmicpc.net/problem/8320
    Input :
        6
    Output :
        8
*/

#include <iostream>
#include <cmath>
#include <cstring>

#define MAX_N 10001

bool available[MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    int count = 0;
    for (int i = 1; i <= n; i++)
    {
        memset(&(available[0]), true, sizeof(bool) * (i + 1));

        int sqrti = (int)sqrt(i);
        for (int j = 1; j <= sqrti; j++)
        {
            if (available[j] && (i % j) == 0)
            {
                int k = i / j;
                available[j] = false;
                available[k] = false;

                count++;
            }
        }
    }

    std::cout << count;

    return 0;
}
