/*
    1546 : 평균
    URL : https://www.acmicpc.net/problem/1546
    Input #1 :
        3
        40 80 60
    Output #1 :
        75.00
    Input #2 :
        3
        10 20 30
    Output #2 :
        66.666667
    Input #3 :
        4
        1 100 100 100
    Output #3 :
        75.25
    Input #4 :
        5
        1 2 4 8 16
    Output #4 :
        38.75
    Input #5 :
        2
        3 10
    Output #5 :
        65.00
*/
#include <iostream>

#define MAX_N 1001

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    int max = 0;
    double sum = 0;
    int scores[MAX_N];

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int score;

        cin >> score;
        scores[i] = score;

        if (score > max)
        {
            max = score;
        }
    }

    for (int i = 0; i < N; i++)
    {
        sum += ((double)scores[i] / (double)max) * 100;
    }

    cout << (sum / N);

    return 0;
}
