/*
    11070 : 피타고라스 기대값
    URL : https://www.acmicpc.net/problem/11070
    Input :
        2
        3 5
        1 2 3 5
        1 3 10 1
        1 2 0 7
        2 3 9 3
        3 2 4 5
        4 6
        1 2 0 11
        1 3 17 13
        1 4 17 1
        2 3 7 12
        2 4 19 17
        3 4 17 0
    Output :
        871
        100
        753
        103
*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;

        vector< pair<int, int> > TEAMS;
        for (int i = 0; i < n; ++i)
        {
            TEAMS.push_back(pair<int, int>(0, 0));
        }
        for (int i = 0; i < m; ++i)
        {
            int a, b, p, q;
            cin >> a >> b >> p >> q;
            TEAMS[a - 1].first += p;
            TEAMS[a - 1].second += q;
            TEAMS[b - 1].first += q;
            TEAMS[b - 1].second += p;
        }

        long long MIN = 987654321;
        long long MAX = 0;
        
        for (int i = 0; i < n; ++i)
        {
            pair<int, int> team = TEAMS[i];
            long long S = team.first * team.first;
            long long A = team.second * team.second;
            long long W;
            if (A == 0)
            {
                if (S == 0)
                {
                    W = 0LL;
                }
                else
                {
                    W = 1000LL;
                }
            }
            else
            {
                W = ((double) S * 1000LL / (double) (S + A));
            }
            if (W < MIN)
            {
                MIN = W;
            }
            if (W > MAX)
            {
                MAX = W;
            }
        }
        cout << MAX << endl;
        cout << MIN << endl;
    }
    return 0;
}