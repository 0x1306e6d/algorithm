/*
    1992 : 쿼드트리
    URL : https://www.acmicpc.net/problem/1992
    Input :
        8
        11110000
        11110000
        00011100
        00011100
        11110000
        11110000
        11110011
        11110011
    Output :
        ((110(0101))(0010)1(0001)) 
*/

#include <iostream>
#include <string>

#define MAX_N 64

int matrix[MAX_N][MAX_N];

std::string quadtree(int x0, int y0, int x1, int y1)
{
    bool white = true;
    bool black = true;
    for (int i = x0; i < x1; i++)
    {
        for (int j = y0; j < y1; j++)
        {
            if (white && (matrix[i][j] == 1))
            {
                white = false;
            }
            if (black && (matrix[i][j] == 0))
            {
                black = false;
            }

            if ((!white) && (!black))
            {
                break;
            }
        }

        if ((!white) && (!black))
        {
            break;
        }
    }

    if (white)
    {
        return std::string("0");
    }
    if (black)
    {
        return std::string("1");
    }

    int x2 = (x0 + x1) / 2;
    int y2 = (y0 + y1) / 2;
    std::string compressed;
    compressed.append("(");
    compressed.append(quadtree(x0, y0, x2, y2));
    compressed.append(quadtree(x0, y2, x2, y1));
    compressed.append(quadtree(x2, y0, x1, y2));
    compressed.append(quadtree(x2, y2, x1, y1));
    compressed.append(")");
    return compressed;
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::string row;
        std::cin >> row;

        for (int j = 0; j < n; j++)
        {
            matrix[i][j] = (row[j] == '1');
        }
    }

    std::cout << quadtree(0, 0, n, n);

    return 0;
}
