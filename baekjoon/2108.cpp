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
int COUNT[MAX_NUMBER];

int partition(int left, int right)
{
    int low = left + 1;
    int high = right;
    int pivot = ARRAY[left];

    while (low <= high)
    {
        while ((low <= right) && ARRAY[low] <= pivot)
        {
            if (low == (N - 1))
            {
                break;
            }
            low++;
        }
        while (((left + 1) <= high) && (ARRAY[high] > pivot))
        {
            high--;
        }

        if (low <= high)
        {
            int temp = ARRAY[low];
            ARRAY[low] = ARRAY[high];
            ARRAY[high] = temp;
        }
        if (low == (N - 1))
        {
            break;
        }
    }

    int temp = ARRAY[left];
    ARRAY[left] = ARRAY[high];
    ARRAY[high] = temp;

    return high;
}

void quicksort(int left, int right)
{
    if (left <= right)
    {
        int pivot = partition(left, right);

        quicksort(left, pivot - 1);
        quicksort(pivot + 1, right);
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

    quicksort(0, N - 1);

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
