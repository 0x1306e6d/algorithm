/*
    9465 : 스티커
    URL : https://www.acmicpc.net/problem/9465
    Input :
        2
        5
        50 10 100 20 40
        30 50 70 10 60
        7
        10 30 10 50 100 20 40
        20 40 30 50 60 20 80
    Output :
        260
        290
*/

#include <iostream>
#include <cstring>

#define MAX_N 100001

int board[2][MAX_N];
int score[2][MAX_N];

int main(int argc, char const *argv[])
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        memset(&(score[0][0]), 0, sizeof(int) * 2 * MAX_N);

        int n;
        std::cin >> n;

        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < n; j++)
            {
                std::cin >> board[i][j];
            }
        }

        score[0][0] = board[0][0];
        score[1][0] = board[1][0];
        score[0][1] = board[0][1] + score[1][0];
        score[1][1] = board[1][1] + score[0][0];
        for (int i = 2; i < n; i++)
        {
            int before = std::max(score[0][i - 2], score[1][i - 2]);
            score[0][i] = board[0][i] + std::max(score[1][i - 1], before);
            score[1][i] = board[1][i] + std::max(score[0][i - 1], before);
        }

        std::cout << std::max(score[0][n - 1], score[1][n - 1]) << std::endl;
    }

    return 0;
}
