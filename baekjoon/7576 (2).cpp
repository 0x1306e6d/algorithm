/*
    7576 : 토마토
    URL : https://www.acmicpc.net/problem/7576
    Input : 
        6 4
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 1
    Output :
        8
*/
#include <iostream>

#define TOMATO_RIPEN 1
#define TOMATO_NOT_RIPEN 0
#define TOMATO_NOT_EXISTS -1
#define TOMATO_RIPING 2

using namespace std;

int main()
{
    int M, N;
    cin >> M;
    cin >> N;

    bool is_all_ripen = true;
    bool has_ripen_tomato = false;
    int storage[N][M];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int state;
            cin >> state;

            storage[i][j] = state;
            if (!has_ripen_tomato && state == TOMATO_RIPEN)
            {
                has_ripen_tomato = true;
            }
            if (is_all_ripen && state == TOMATO_NOT_RIPEN)
            {
                is_all_ripen = false;
            }
        }
    }
    if (is_all_ripen)
    {
        cout << 0;
        return 0;
    }

    bool is_impossible = false;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int tomato = storage[i][j];
            int neighbor_count = 0;
            int isolation_count = 0;
            if (tomato == TOMATO_NOT_RIPEN)
            {
                // Top
                if (i > 0)
                {
                    neighbor_count++;
                    if (storage[i - 1][j] == TOMATO_NOT_EXISTS)
                    {
                        isolation_count++;
                    }
                }
                // Bottom
                if (i < (N - 1))
                {
                    neighbor_count++;
                    if (storage[i + 1][j] == TOMATO_NOT_EXISTS)
                    {
                        isolation_count++;
                    }
                }
                // Left
                if (j > 0)
                {
                    neighbor_count++;
                    if (storage[i][j - 1] == TOMATO_NOT_EXISTS)
                    {
                        isolation_count++;
                    }
                }
                // Right
                if (j < (M - 1))
                {
                    neighbor_count++;
                    if (storage[i][j + 1] == TOMATO_NOT_EXISTS)
                    {
                        isolation_count++;
                    }
                }

                if (neighbor_count == isolation_count)
                {
                    is_impossible = true;
                    break;
                }
            }

            if (is_impossible)
            {
                break;
            }
        }
    }
    if (is_impossible || !has_ripen_tomato)
    {
        cout << -1;
        return 0;
    }

    int day = 0;
    while (true)
    {
        day++;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                int tomato = storage[i][j];
                if (tomato == TOMATO_RIPEN)
                {
                    // Top
                    if (i > 0)
                    {
                        if (storage[i - 1][j] == TOMATO_NOT_RIPEN)
                        {
                            storage[i - 1][j] = TOMATO_RIPING;
                        }
                    }
                    // Bottom
                    if (i < (N - 1))
                    {
                        if (storage[i + 1][j] == TOMATO_NOT_RIPEN)
                        {
                            storage[i + 1][j] = TOMATO_RIPING;
                        }
                    }
                    // Left
                    if (j > 0)
                    {
                        if (storage[i][j - 1] == TOMATO_NOT_RIPEN)
                        {
                            storage[i][j - 1] = TOMATO_RIPING;
                        }
                    }
                    // Right
                    if (j < (M - 1))
                    {
                        if (storage[i][j + 1] == TOMATO_NOT_RIPEN)
                        {
                            storage[i][j + 1] = TOMATO_RIPING;
                        }
                    }
                }
            }
        }

        is_all_ripen = true;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                int tomato = storage[i][j];
                if (tomato == TOMATO_RIPING)
                {
                    storage[i][j] = TOMATO_RIPEN;
                }
                if (is_all_ripen && tomato == TOMATO_NOT_RIPEN)
                {
                    is_all_ripen = false;
                }
            }
        }

        if (is_all_ripen)
        {
            cout << day;
            return 0;
        }
    }

    return 0;
}