/*
    1051 : 숫자 정사각형
    URL : https://www.acmicpc.net/problem/1051
    Input :
        3 5
        42101
        22100
        22101
    Output :
        9
*/

#include <iostream>

#define MAX_N 51
#define MAX_M 51

int n;
int m;
int matrix[MAX_N][MAX_M];

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            char c;
            std::cin >> c;

            matrix[i][j] = int(c - '0');
        }
    }

    int maxSize = 1;
    int dLimit = std::min(n, m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            for (int d = 1; d <= dLimit; d++)
            {
                int x = (j + d);
                int y = (i + d);

                if ((x < m) && (y < n))
                {
                    if ((matrix[i][j] == matrix[i][x]) &&
                        (matrix[i][j] == matrix[y][j]) &&
                        (matrix[i][j] == matrix[y][x]))
                    {
                        maxSize = std::max(maxSize, (x - j + 1) * (y - i + 1));
                    }
                }
                else
                {
                    break;
                }
            }
        }
    }

    std::cout << maxSize;

    return 0;
}
