/*
    11067 : 모노톤길 
    URL : https://www.acmicpc.net/problem/11067
    Input : 
        2
        17
        3 3
        5 3
        11 2
        9 2
        2 1
        3 1
        5 1
        0 0
        1 0
        2 0
        9 0
        11 -1
        9 -3
        6 -1
        7 -1
        7 -3
        5 -1
        3 5 14 17
        4
        0 0
        0 1
        1 1
        1 0
        5 1 4 1 3 1
    Output : 
        3 1
        9 0
        11 -1
        0 0
        1 0
        0 0
        1 1
        0 0
*/

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 100000

using namespace std;

pair<int, int> TABLE[MAX];

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            int x, y;
            cin >> x >> y;
            TABLE[i] = pair<int, int>(x, y);
        }

        sort(TABLE, TABLE + n);

        int start_index = 0;
        int end_index = 0;
        for (int i = 0; i < n; ++i)
        {
            pair<int, int> current = TABLE[i];
            pair<int, int> next = TABLE[i + 1];
            if (current.first == next.first)
            {
                end_index = end_index + 1;
            }
            else
            {
                if (abs(TABLE[start_index].second - TABLE[start_index - 1].second) > abs(current.second - TABLE[start_index - 1].second))
                {
                    reverse(TABLE + start_index, TABLE + end_index + 1);
                }
                start_index = i + 1;
                end_index = start_index;
            }
        }

        int m;
        cin >> m;
        while (m--)
        {
            int number;
            cin >> number;
            pair<int, int> cafe = TABLE[number - 1];
            cout << cafe.first << ' ' << cafe.second << endl;
        }
    }
    return 0;
}