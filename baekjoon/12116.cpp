/*
    12116 : Uzastopni
    URL : https://www.acmicpc.net/problem/12116
    Input #1 :
        10
    Output #1 :
        1 4
    Input #2 :
        27
    Output #2 :
        13 14
        8 10
        2 7
*/

#include <iostream>
#include <cstdint>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);

    uint64_t sum = 0;
    int i = 1;
    for (int j = 1; j <= (n / 2) + 1; j++)
    {
        sum += j;

        while (sum > n)
        {
            sum -= i;
            i += 1;
        }

        if (sum == n)
        {
            printf("%d %d\n", i, j);
        }
    }

    return 0;
}
