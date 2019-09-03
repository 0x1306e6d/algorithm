/*
    2108 : 통계학
    URL : https://www.acmicpc.net/problem/2108
    Input #1 :
        5
        1
        3
        8
        -2
        2
    Output #1 :
        2
        2
        1
        10
    Input #2 :
        1
        4000
    Output #2 :
        4000
        4000
        4000
        0
    Input #3 :
        5
        -1
        -2
        -3
        -1
        -2
    Output #3 :
        -2
        -2
        -1
        2
*/

#include <iostream>
#include <limits>
#include <cmath>
#include <cstring>

#define MAX_N 500001
#define MAX_NUMBER 8002

using namespace std;

int N;
int ARRAY[MAX_N];
int TEMP[MAX_N];
int COUNT[MAX_NUMBER];

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while ((i <= mid) && (j <= right))
    {
        if (ARRAY[i] <= ARRAY[j])
        {
            TEMP[k] = ARRAY[i];
            i++;
        }
        else
        {
            TEMP[k] = ARRAY[j];
            j++;
        }
        k++;
    }

    if (i > mid)
    {
        for (int l = j; l <= right; l++)
        {
            TEMP[k] = ARRAY[l];
            k++;
        }
    }
    else
    {
        for (int l = i; l <= mid; l++)
        {
            TEMP[k] = ARRAY[l];
            k++;
        }
    }

    for (int l = left; l <= right; l++)
    {
        ARRAY[l] = TEMP[l];
    }
}

void msort(int left, int right)
{
    if (left < right)
    {
        int mid = (left + right) / 2;
        msort(left, mid);
        msort(mid + 1, right);

        merge(left, mid, right);
    }
}

int main(int argc, char const *argv[])
{
    int sum = 0;
    int modeCount = numeric_limits<int>::min();

    memset(&(COUNT[0]), 0, sizeof(int) * MAX_NUMBER);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> ARRAY[i];

        sum += ARRAY[i];

        COUNT[4000 + ARRAY[i]] += 1;
        if (COUNT[4000 + ARRAY[i]] > modeCount)
        {
            modeCount = COUNT[4000 + ARRAY[i]];
        }
    }

    msort(0, N - 1);

    bool first = false;
    int mode = numeric_limits<int>::min();
    for (int i = 0; i < MAX_NUMBER; i++)
    {
        if (COUNT[i] == modeCount)
        {
            mode = i - 4000;

            if (first)
            {
                break;
            }
            else
            {
                first = true;
            }
        }
    }

    cout << round((float)sum / (float)N) << endl;
    cout << ARRAY[N / 2] << endl;
    cout << mode << endl;
    cout << (ARRAY[N - 1] - ARRAY[0]) << endl;

    return 0;
}
