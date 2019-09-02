/*
    2630 : 색종이 만들기
    URL : https://www.acmicpc.net/problem/2630
    Input :
        8
        1 1 0 0 0 0 1 1
        1 1 0 0 0 0 1 1
        0 0 0 0 1 1 0 0
        0 0 0 0 1 1 0 0
        1 0 0 0 1 1 1 1
        0 1 0 0 1 1 1 1
        0 0 1 1 1 1 1 1
        0 0 1 1 1 1 1 1
    Output :
        9
        7
*/

#include <iostream>

#define MAX_N 129

int white = 0;
int blue = 0;
int matrix[MAX_N][MAX_N];

void count(int x1, int x2, int y1, int y2)
{
    bool isWhite = true;
    bool isblue = true;

    for (int y = y1; y < y2; y++)
    {
        for (int x = x1; x < x2; x++)
        {
            if (matrix[y][x] == 0)
            {
                isblue = false;
            }
            else
            {
                isWhite = false;
            }

            if (!isblue && !isWhite)
            {
                break;
            }
        }
    }

    if (isblue)
    {
        blue++;
    }
    else if (isWhite)
    {
        white++;
    }
    else
    {
        int x3 = (x1 + x2) / 2;
        int y3 = (y1 + y2) / 2;

        count(x1, x3, y1, y3);
        count(x3, x2, y1, y3);
        count(x1, x3, y3, y2);
        count(x3, x2, y3, y2);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            std::cin >> matrix[y][x];
        }
    }

    count(0, n, 0, n);

    std::cout << white << std::endl;
    std::cout << blue << std::endl;

    return 0;
}
