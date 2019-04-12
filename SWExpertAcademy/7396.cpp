/*
    7396 : 종구의 딸이름 짓기
    Input :
        3
        2 5
        adbfc
        dcghi
        5 5
        bbbbb
        bbbbb
        bazbb
        bzbbb
        bbbbb
        4 5
        ponoc
        ohoho
        hlepo
        mirko
    Output :
        #1 adbfci
        #2 bbbazbbbb
        #3 pohlepko
*/

#include <iostream>
#include <string>

#define MAX_N 2001
#define MAX_M 2001

int N;
int M;
char board[MAX_N][MAX_M];
std::string dp[2][MAX_M];

int main(void)
{
    std::ios::sync_with_stdio(false);

    for (int x = 0; x < M; x++)
    {
        dp[0][x].reserve(MAX_N + MAX_M);
        dp[1][x].reserve(MAX_N + MAX_M);
    }

    int T;
    std::cin >> T;

    for (int t = 1; t <= T; t++)
    {
        std::cin >> N;
        std::cin >> M;

        for (int x = 0; x < M; x++)
        {
            dp[0][x].clear();
            dp[1][x].clear();
        }

        for (int y = 0; y < N; y++)
        {
            for (int x = 0; x < M; x++)
            {
                std::cin >> board[y][x];
            }
        }

        dp[0][0] += board[0][0];
        for (int x = 1; x < M; x++)
        {
            dp[0][x] = dp[0][x - 1];
            dp[0][x] += board[0][x];
        }
        for (int y = 1; y < N; y++)
        {
            int current = (y % 2);
            int top = ((y - 1) % 2);
            dp[current][0] = dp[top][0];
            dp[current][0].push_back(board[y][0]);

            for (int x = 1; x < M; x++)
            {
                int left = (x - 1);
                if (dp[top][x] < dp[y % 2][left])
                {
                    dp[current][x] = dp[top][x];
                    dp[current][x].push_back(board[y][x]);
                }
                else
                {
                    dp[current][x] = dp[current][left];
                    dp[current][x].push_back(board[y][x]);
                }
            }
        }

        std::cout << "#" << t << " " << dp[(N - 1) % 2][M - 1] << '\n';
    }

    return 0;
}