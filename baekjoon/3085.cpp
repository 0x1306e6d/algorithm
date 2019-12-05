/*
    3085 : 사탕 게임
    URL : https://www.acmicpc.net/problem/3085
    Input :
        5
        YCPZY
        CYZZP
        CCPPP
        YCYZC
        CPPZZ
    Output :
        4
*/

#include <iostream>

#define MAX_N 51

const int dxs[] = {-1, 1, 0, 0};
const int dys[] = {0, 0, -1, 1};

int board[MAX_N][MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::string s;
        std::cin >> s;

        for (int j = 0; j < n; j++)
        {
            board[i][j] = s.at(j);
        }
    }

    int count = 0;
    int last = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int columnCount = 0;
            for (int k = 0; k < n; k++)
            {
                if (last == board[k][j])
                {
                    columnCount++;
                }
                else
                {
                    count = std::max(count, columnCount);

                    last = board[k][j];
                    columnCount = 1;
                }
            }
            count = std::max(count, columnCount);

            last = 0;
            int rowCount = 0;
            for (int k = 0; k < n; k++)
            {
                if (last == board[i][k])
                {
                    rowCount++;
                }
                else
                {
                    count = std::max(count, rowCount);

                    last = board[i][k];
                    rowCount = 1;
                }
            }
            count = std::max(count, rowCount);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int d = 0; d < 4; d++)
            {
                int dx = dxs[d];
                int dy = dys[d];

                int x = j + dx;
                int y = i + dy;
                if ((x >= 0) && (x < n) && (y >= 0) && (y < n))
                {
                    if (board[i][j] != board[y][x])
                    {
                        int temp = board[i][j];
                        board[i][j] = board[y][x];
                        board[y][x] = temp;

                        last = 0;
                        int columnCount = 0;
                        for (int k = 0; k < n; k++)
                        {
                            if (last == board[k][j])
                            {
                                columnCount++;
                            }
                            else
                            {
                                count = std::max(count, columnCount);

                                last = board[k][j];
                                columnCount = 1;
                            }
                        }
                        count = std::max(count, columnCount);

                        last = 0;
                        int rowCount = 0;
                        for (int k = 0; k < n; k++)
                        {
                            if (last == board[i][k])
                            {
                                rowCount++;
                            }
                            else
                            {
                                count = std::max(count, rowCount);

                                last = board[i][k];
                                rowCount = 1;
                            }
                        }
                        count = std::max(count, rowCount);

                        temp = board[i][j];
                        board[i][j] = board[y][x];
                        board[y][x] = temp;
                    }
                }
            }
        }
    }

    std::cout << count;

    return 0;
}
