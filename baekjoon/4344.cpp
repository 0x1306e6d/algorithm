/*
    4344 : 평균은 넘겠지
    URL : https://www.acmicpc.net/problem/4344
    Input :
        5
        5 50 50 70 80 100
        7 100 95 90 80 70 60 50
        3 70 90 80
        3 70 90 81
        9 100 99 98 97 96 95 94 93 91
    Output :
        40.000%
        57.143%
        33.333%
        66.667%
        55.556%
*/
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int C;

    cout << fixed;
    cout.precision(3);

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int N;
        int sum = 0;
        int count = 0;
        double average;
        int *scores;

        cin >> N;
        scores = new int[N];

        for (int i = 0; i < N; i++)
        {
            int score;

            cin >> score;
            sum += score;
            scores[i] = score;
        }

        average = (double)sum / (double)N;

        for (int i = 0; i < N; i++)
        {
            if (scores[i] > average)
            {
                count += 1;
            }
        }

        cout << (((double)count / (double)N) * 100) << '%' << endl;
    }

    return 0;
}
