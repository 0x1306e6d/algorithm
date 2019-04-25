/*
    2740 : 행렬 곱셈
    URL : https://www.acmicpc.net/problem/2740
    Input :
        3 2
        1 2
        3 4
        5 6
        2 3
        -1 -2 0
        0 0 3
    Output :
        -1 -2 6
        -3 -6 12
        -5 -10 18
*/

#include <iostream>

#define MAX_N 101
#define MAX_M 101
#define MAX_K 101

int n;
int m;
int k;

int matrixA[MAX_N][MAX_M];
int matrixB[MAX_M][MAX_K];
int matrixC[MAX_N][MAX_K];

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cin >> matrixA[i][j];
        }
    }

    std::cin >> m;
    std::cin >> k;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < k; j++)
        {
            std::cin >> matrixB[i][j];
        }
    }    

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < k; j++)
        {
            matrixC[i][j] = 0;

            for (int l = 0; l < m; l++)
            {
                matrixC[i][j] += (matrixA[i][l] * matrixB[l][j]);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < k; j++)
        {
            std::cout << matrixC[i][j] << ' ';
        }
        std::cout << std::endl;
    }

    return 0;
}
