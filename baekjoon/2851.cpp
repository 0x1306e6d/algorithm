/*
    2851 : 슈퍼 마리오
    URL : https://www.acmicpc.net/problem/2851
    Input :
        10
        20
        30
        40
        50
        60
        70
        80
        90
        100
    Output :
        100
*/

#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int score = 0;
    for (int i = 0; i < 10; i++)
    {
        int mushroom;
        cin >> mushroom;

        int before = abs(100 - score);
        int after = abs(100 - score - mushroom);
        if (before > after)
        {
            score += mushroom;
        }
        else if (before < after)
        {
            cout << score;
            return 0;
        }
        else
        {
            cout << (score + mushroom);
            return 0;
        }
    }
    cout << score;
    return 0;
}