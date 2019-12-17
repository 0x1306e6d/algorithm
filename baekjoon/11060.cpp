/*
    11060 : 점프 점프
    URL : https://www.acmicpc.net/problem/11060
    Input :
        10
        1 2 0 1 3 2 1 5 4 2
    Output :
        5
*/

#include <iostream>

#define MAX_N 1001

int n;
int maze[MAX_N];
int cache[MAX_N];

int go(int here)
{
    int &ret = cache[here];
    if (ret != 0)
    {
        return ret;
    }

    if (here == (n - 1))
    {
        return 0;
    }

    int countHere = 987654321;
    for (int i = 1; i <= maze[here]; i++)
    {
        if ((here + i) < n)
        {
            int countThere = go(here + i);
            if (countThere != -1)
            {
                countHere = std::min(countHere, 1 + countThere);
            }
        }
    }
    if (countHere == 987654321)
    {
        ret = -1;
    }
    else
    {
        ret = countHere;
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        std::cin >> maze[i];

        cache[i] = 0;
    }

    std::cout << go(0);

    return 0;
}
