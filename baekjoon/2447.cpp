/*
    2447 : 별 찍기 - 10
    URL : https://www.acmicpc.net/problem/2447
    Input :
        27
    Output :
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        ***   ******   ******   ***
        * *   * ** *   * ** *   * *
        ***   ******   ******   ***
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        *********         *********
        * ** ** *         * ** ** *
        *********         *********
        ***   ***         ***   ***
        * *   * *         * *   * *
        ***   ***         ***   ***
        *********         *********
        * ** ** *         * ** ** *
        *********         *********
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
        ***   ******   ******   ***
        * *   * ** *   * ** *   * *
        ***   ******   ******   ***
        ***************************
        * ** ** ** ** ** ** ** ** *
        ***************************
*/

#include <iostream>

#define MAX_N 6561

bool matrix[MAX_N][MAX_N];

void draw(int x, int y, int n)
{
    if (n == 3)
    {
        for (int i = x; i < (x + 3); i++)
        {
            matrix[y][i] = true;
            matrix[y + 2][i] = true;
        }
        matrix[y + 1][x] = true;
        matrix[y + 1][x + 2] = true;
    }
    else
    {
        int m = (n / 3);
        int x0 = x;
        int x1 = x + m;
        int x2 = x + (m * 2);
        int y0 = y;
        int y1 = y + m;
        int y2 = y + (m * 2);

        draw(x0, y0, m);
        draw(x1, y0, m);
        draw(x2, y0, m);
        draw(x0, y1, m);
        draw(x2, y1, m);
        draw(x0, y2, m);
        draw(x1, y2, m);
        draw(x2, y2, m);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    draw(0, 0, n);

    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            if (matrix[y][x])
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
