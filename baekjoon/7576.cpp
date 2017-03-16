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
#include <vector>

#define TOMATO_RIPEN 1
#define TOMATO_NOT_RIPEN 0
#define TOMATO_NOT_EXISTS -1

using namespace std;

int main()
{
    int M, N;
    cin >> M;
    cin >> N;

    bool is_all_ripen = true;
    bool has_ripen_tomato = false;
    int storage[N][M];
    int tomato_count = 0;
    vector< pair<int, int> > ripens;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int state;
            cin >> state;

            storage[i][j] = state;
            if (state == TOMATO_RIPEN)
            {
                ripens.push_back(make_pair(i, j));
                tomato_count++;
                if (!has_ripen_tomato)
                {
                    has_ripen_tomato = true;
                }
            }
            if (state == TOMATO_NOT_RIPEN)
            {
                tomato_count++;
                if (is_all_ripen)
                {
                    is_all_ripen = false;
                }
            }
        }
    }
    if (is_all_ripen)
    {
        cout << 0;
        return 0;
    }
    else if (!has_ripen_tomato)
    {
        cout << -1;
        return 0;
    }

    int day = 0;
    int last_ripen_count = ripens.size();
    while (true)
    {
        day++;

        for (int i = 0; i < last_ripen_count; i++)
        {
            pair<int, int> tomato = ripens.at(i);
            int y = tomato.first;
            int x = tomato.second;

            // Top
            if (y > 0)
            {
                if (storage[y - 1][x] == TOMATO_NOT_RIPEN)
                {
                    storage[y - 1][x] = TOMATO_RIPEN;
                    ripens.push_back(make_pair(y - 1, x));
                }
            }
            // Bottom
            if (y < (N - 1))
            {
                if (storage[y + 1][x] == TOMATO_NOT_RIPEN)
                {
                    storage[y + 1][x] = TOMATO_RIPEN;
                    ripens.push_back(make_pair(y + 1, x));
                }
            }
            // Left
            if (x > 0)
            {
                if (storage[y][x - 1] == TOMATO_NOT_RIPEN)
                {
                    storage[y][x - 1] = TOMATO_RIPEN;
                    ripens.push_back(make_pair(y, x - 1));
                }
            }
            // Right
            if (x < (M - 1))
            {
                if (storage[y][x + 1] == TOMATO_NOT_RIPEN)
                {
                    storage[y][x + 1] = TOMATO_RIPEN;
                    ripens.push_back(make_pair(y, x + 1));
                }
            }
        }

        int new_count = ripens.size();
        if (last_ripen_count == new_count)
        {
            cout << -1;
            return 0;
        }

        last_ripen_count = new_count;
        if (last_ripen_count == tomato_count)
        {
            cout << day;
            return 0;
        }
    }

    return 0;
}