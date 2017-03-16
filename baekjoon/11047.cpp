/*
    11047 : 동전 0
    URL : https://www.acmicpc.net/problem/11047
    Input #1 :
        10 4200
        1
        5
        10
        50
        100
        500
        1000
        5000
        10000
        50000
    Output #1 :
        6
    Input #2 :
        10 4790
        1
        5
        10
        50
        100
        500
        1000
        5000
        10000
        50000
    Output #2 :
        12
*/
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;
    vector<int> coins;

    cin >> N;
    cin >> K;
    while (N--)
    {
        int value;
        cin >> value;
        coins.push_back(value);
    }

    int count = 0;
    vector<int>::reverse_iterator it = coins.rbegin();
    while (K >= 0 && it != coins.rend())
    {
        int value = *it;
        if (K >= value)
        {
            count++;
            K = K - value;
        }
        else
        {
            ++it;
        }
    }

    cout << count;

    return 0;
}