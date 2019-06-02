/*
    1717: 집합의 표현
    URL : https://www.acmicpc.net/problem/1717
    Input :
        7 8
        0 1 3
        1 1 7
        0 7 6
        1 7 1
        0 3 7
        0 4 2
        0 1 1
        1 1 1
    Output :
        NO
        NO
        YES
*/

#include <iostream>

#define MAX_N 1000001

int parents[MAX_N];
int ranks[MAX_N];

int find(int i)
{
    if (i == parents[i])
    {
        return i;
    }
    else
    {
        int j = find(parents[i]);
        parents[i] = j;
        return j;
    }
}

void merge(int i, int j)
{
    i = find(i);
    j = find(j);

    if (i == j)
    {
        return;
    }

    if (ranks[i] > ranks[j])
    {
        std::swap(i, j);
    }

    parents[i] = j;

    if (ranks[i] == ranks[j])
    {
        ranks[j]++;
    }
}

int main(int argc, char const *argv[])
{
    std::ios::sync_with_stdio(false);

    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i < (n + 1); i++)
    {
        parents[i] = i;
    }

    int c;
    int a;
    int b;
    for (int i = 0; i < m; i++)
    {
        std::cin >> c;
        std::cin >> a;
        std::cin >> b;

        if (c == 0)
        {
            merge(a, b);
        }
        else
        {
            a = find(a);
            b = find(b);

            if (a == b)
            {
                std::cout << "YES\n";
            }
            else
            {
                std::cout << "NO\n";
            }
        }
    }

    return 0;
}
