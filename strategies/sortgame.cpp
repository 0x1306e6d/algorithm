/*
    SORTGAME : Sorting Game
    Difficulty : 중
    Input :
        3
        8
        1 2 3 4 8 7 6 5
        4
        3 4 1 2
        3
        1 2 3
    Output :
        1
        2
        0
*/

#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>

std::map<std::vector<int>, int> presorted;

void precalc(int n)
{
    std::vector<int> sequence(n);
    for (int i = 0; i < n; i++)
    {
        sequence[i] = i;
    }

    std::queue<std::vector<int>> q;
    q.push(sequence);
    presorted[sequence] = 0;

    while (!q.empty())
    {
        std::vector<int> here = q.front();
        q.pop();

        int cost = presorted[here];
        for (int i = 0; i < n; i++)
        {
            for (int j = (i + 2); j <= n; j++)
            {
                std::reverse(here.begin() + i, here.begin() + j);
                if (presorted.count(here) == 0)
                {
                    presorted[here] = (cost + 1);
                    q.push(here);
                }
                std::reverse(here.begin() + i, here.begin() + j);
            }
        }
    }
}

int sortgame(const std::vector<int> &sequence)
{
    int nsequence = sequence.size();
    std::vector<int> fixed(nsequence);

    for (int i = 0; i < nsequence; i++)
    {
        int smaller = 0;
        for (int j = 0; j < nsequence; j++)
        {
            if (sequence[j] < sequence[i])
            {
                smaller++;
            }
        }
        fixed[i] = smaller;
    }

    return presorted[fixed];
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int i = 1; i <= 8; i++)
    {
        precalc(i);
    }

    for (int c = 0; c < C; c++)
    {
        int n;
        std::cin >> n;

        std::vector<int> sequence(n, 0);

        for (int i = 0; i < n; i++)
        {
            std::cin >> sequence[i];
        }

        std::cout << sortgame(sequence) << std::endl;
    }

    return 0;
}
