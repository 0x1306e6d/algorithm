/*
    14501 : 퇴사
    URL : https://www.acmicpc.net/problem/14501
    Input #1 :
        7
        3 10
        5 20
        1 10
        1 20
        2 15
        4 40
        2 200
    Output #1 :
        45
    Input #2 :
        10
        1 1
        1 2
        1 3
        1 4
        1 5
        1 6
        1 7
        1 8
        1 9
        1 10
    Output #2 :
        55
    Input #3 :
        10
        5 10
        5 9
        5 8
        5 7
        5 6
        5 10
        5 9
        5 8
        5 7
        5 6
    Output #3 :
        20
    Input #4 :
        10
        5 50
        4 40
        3 30
        2 20
        1 10
        1 10
        2 20
        3 30
        4 40
        5 50
    Output #4 :
        90
*/

#include <iostream>

#define MAX_N 16

int n;
int schedule[MAX_N][2];

int consult(int day)
{
    if (day == n)
    {
        return 0;
    }

    int profit = 0;
    for (int next = day; next < n; next++)
    {
        int t = schedule[next][0];
        int p = schedule[next][1];

        if ((next + t) <= n)
        {
            profit = std::max(profit, p + consult(next + t));
        }
    }
    return profit;
}

int main(int argc, char const *argv[])
{
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        int t;
        int p;

        std::cin >> t;
        std::cin >> p;

        schedule[i][0] = t;
        schedule[i][1] = p;
    }

    std::cout << consult(0);

    return 0;
}
