/*
    1018 : 체스판 다시 칠하기
    URL : https://www.acmicpc.net/problem/1018
    Input #1 :
        8 8
        WBWBWBWB
        BWBWBWBW
        WBWBWBWB
        BWBBBWBW
        WBWBWBWB
        BWBWBWBW
        WBWBWBWB
        BWBWBWBW
    Output #1 :
        1
    Input #2 :
        10 13
        BBBBBBBBWBWBW
        BBBBBBBBBWBWB
        BBBBBBBBWBWBW
        BBBBBBBBBWBWB
        BBBBBBBBWBWBW
        BBBBBBBBBWBWB
        BBBBBBBBWBWBW
        BBBBBBBBBWBWB
        WWWWWWWWWWBWB
        WWWWWWWWWWBWB
    Output #2 :
        12
*/

#include <iostream>

#define MAX_N 51
#define MAX_M 51

int n;
int m;

int board[MAX_N][MAX_M];

int chess(int x, int y)
{
    int blackCount = 0;
    int whiteCount = 0;
    for (int i = y; i < (y + 8); i++)
    {
        for (int j = x; j < (x + 8); j++)
        {
            if ((i % 2) == 0)
            {
                if ((j % 2) == 0)
                {
                    if (board[i][j])
                    {
                        blackCount++;
                    }
                    else
                    {
                        whiteCount++;
                    }
                }
                else
                {
                    if (board[i][j])
                    {
                        whiteCount++;
                    }
                    else
                    {
                        blackCount++;
                    }
                }
            }
            else
            {
                if ((j % 2) == 0)
                {
                    if (board[i][j])
                    {
                        whiteCount++;
                    }
                    else
                    {
                        blackCount++;
                    }
                }
                else
                {
                    if (board[i][j])
                    {
                        blackCount++;
                    }
                    else
                    {
                        whiteCount++;
                    }
                }
            }
        }
    }
    return std::min(blackCount, whiteCount);
}

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < n; i++)
    {
        std::string row;
        std::cin >> row;

        for (int j = 0; j < m; j++)
        {
            board[i][j] = (row[j] == 'W');
        }
    }

    int count = (MAX_N * MAX_M);
    for (int i = 0; i <= (n - 8); i++)
    {
        for (int j = 0; j <= (m - 8); j++)
        {
            count = std::min(count, chess(j, i));
        }
    }

    std::cout << count;

    return 0;
}
