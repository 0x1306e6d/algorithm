/*
    1011 : Fly me to the Alpha Centauri
    URL : https://www.acmicpc.net/problem/1011
    Input :
        3
        0 3
        1 5
        45 50
    Output :
        3
        3
        4
*/

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int x;
        int y;

        cin >> x;
        cin >> y;

        int distance = y - x;
        int n = sqrt(distance);

        if (distance == pow(n, 2))
        {
            printf("%d\n", (2 * n) - 1);
        }
        else
        {
            if (distance > (pow(n, 2) + n))
            {
                printf("%d\n", (2 * n) + 1);
            }
            else
            {
                printf("%d\n", 2 * n);
            }
        }
    }

    return 0;
}
