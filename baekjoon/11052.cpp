/*
    11052 : 카드 구매하기
    URL : https://www.acmicpc.net/problem/11052
    Input #1 :
        4
        1 5 6 7
    Output #1 :
        10
    Input #2 :
        5
        10 9 8 7 6
    Output #2 :
        50
    Input #3 :
        10
        1 1 2 3 5 8 13 21 34 55
    Output #3 :
        55
    Input #4 :
        10
        5 10 11 12 13 30 35 40 45 47
    Output #4 :
        50
    Input #5 :
        4
        5 2 8 10
    Output #5 :
        20
    Input #6 :
        4
        3 5 15 16
    Output #6 :
        18
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

int n;
int cards[MAX_N];
int cache[MAX_N][MAX_N];

int blackcow(int i, int k)
{
    if (i > n)
    {
        return 0;
    }

    int &price = cache[i][k];
    if (price != -1)
    {
        return price;
    }

    price = 0;
    int j = 0;
    int l = k;
    do
    {
        price = std::max(price, (j * cards[i]) + blackcow(i + 1, l));
        l -= i;
        j++;
    } while (l >= 0);

    return price;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

    std::cin >> n;

    for (int i = 1; i <= n; i++)
    {
        std::cin >> cards[i];
    }

    std::cout << blackcow(1, n);

    return 0;
}
