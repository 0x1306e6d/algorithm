/*
    7576 : 토마토
    URL : https://www.acmicpc.net/problem/7576
    Input #1 :
        6 4
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 1
    Output #1 :
        8
    Input #2 :
        6 4
        0 -1 0 0 0 0
        -1 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 1
    Output #2 :
        -1
    Input #3 :
        6 4
        1 -1 0 0 0 0
        0 -1 0 0 0 0
        0 0 0 0 -1 0
        0 0 0 0 -1 1
    Output #3 :
        6
    Input #4 :
        5 5
        -1 1 0 0 0
        0 -1 -1 -1 0
        0 -1 -1 -1 0
        0 -1 -1 -1 0
        0 0 0 0 0
    Output #4 :
        14
    Input #5 :
        2 2
        1 -1
        -1 1
    Output #5 :
        0
*/
#include <iostream>
#include <queue>

using namespace std;

#define TOMATO_RIPEN 1
#define TOMATO_NOT_RIPEN 0
#define TOMATO_NOT_EXISTS -1

typedef pair<int, int> Point;

int main()
{
    queue<Point> frontier;

    int M;
    int N;
    cin >> M;
    cin >> N;

    int storage[N][M];
    int goal = 0;
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < M; x++)
        {
            int tomato;
            cin >> tomato;

            storage[y][x] = tomato;
            if (tomato == TOMATO_RIPEN)
            {
                frontier.push(make_pair(x, y));
            }
            else if (tomato == TOMATO_NOT_RIPEN)
            {
                goal++;
            }
        }
    }

    int day = 0;
    while (goal > 0)
    {
        day++;

        int initial_size = frontier.size();
        if (initial_size == 0)
        {
            cout << -1;
            return 0;
        }

        for (int i = 0; i < initial_size; i++)
        {
            Point tomato = frontier.front();
            frontier.pop();
            int x = tomato.first;
            int y = tomato.second;

            // Top
            if (y > 0)
            {
                if (storage[y - 1][x] == TOMATO_NOT_RIPEN)
                {
                    storage[y - 1][x] = TOMATO_RIPEN;
                    goal--;
                    frontier.push(make_pair(x, y - 1));
                }
            }
            // Bottom
            if (y < (N - 1))
            {
                if (storage[y + 1][x] == TOMATO_NOT_RIPEN)
                {
                    storage[y + 1][x] = TOMATO_RIPEN;
                    goal--;
                    frontier.push(make_pair(x, y + 1));
                }
            }
            // Left
            if (x > 0)
            {
                if (storage[y][x - 1] == TOMATO_NOT_RIPEN)
                {
                    storage[y][x - 1] = TOMATO_RIPEN;
                    goal--;
                    frontier.push(make_pair(x - 1, y));
                }
            }
            // Right
            if (x < (M - 1))
            {
                if (storage[y][x + 1] == TOMATO_NOT_RIPEN)
                {
                    storage[y][x + 1] = TOMATO_RIPEN;
                    goal--;
                    frontier.push(make_pair(x + 1, y));
                }
            }
        }
    }

    cout << day;

    return 0;
}