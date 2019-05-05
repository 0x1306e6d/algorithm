/*
    1436 : 영화감독 숌
    URL : https://www.acmicpc.net/problem/1436
    Input :
        2
    Output :
        1666
*/

#include <iostream>

#define MAX_N 10001

int numbers[MAX_N];

bool is666(int i)
{
    while (i != 0)
    {
        if ((i % 1000) == 666)
        {
            return true;
        }
        i = (i / 10);
    }
    return false;
}

int main(int argc, char const *argv[])
{
    int number;
    numbers[1] = 666;
    numbers[2] = 1666;
    for (int i = 3; i < MAX_N; i++)
    {
        number = numbers[i - 1] + 1;
        while (!is666(number))
        {
            number++;
        }
        numbers[i] = number;
    }

    int n;
    std::cin >> n;
    std::cout << numbers[n];

    return 0;
}
