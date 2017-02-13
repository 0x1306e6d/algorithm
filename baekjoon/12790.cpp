/*
    12790 : Mini Fantasy War
    URL : https://www.acmicpc.net/problem/12790
    Input :
        3
        100 100 100 100 0 0 0 0
        10 20 30 40 40 30 20 10
        100 100 100 100 -200 0 400 400
    Output :
        1000
        500
        2501
*/
#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int hp, mp, atk, def;
        int incHp, incMp, incAtk, incDef;
        cin >> hp >> mp >> atk >> def;
        cin >> incHp >> incMp >> incAtk >> incDef;

        hp = max(hp + incHp, 1);
        mp = max(mp + incMp, 1);
        atk = max(atk + incAtk, 0);
        def = def + incDef;

        int power = hp + (5 * mp) + (2 * atk) + (2 * def);
        cout << power << endl;
    }

    return 0;
}