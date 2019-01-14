/*
    2751 : 수 정렬하기 2
    URL : https://www.acmicpc.net/problem/2751
    Input :
        5
        5
        4
        3
        2
        1
    Output :
        1
        2
        3
        4
        5
*/

#include <iostream>

#define MAX_N 1000001

using namespace std;

int N;
int ARRAY[MAX_N];

void qsort(int low, int high)
{
    int i = low;
    int j = high;
    int pivot = ARRAY[(low + high) / 2];

    do
    {
        while (ARRAY[i] < pivot && i <= high)
        {
            i++;
        }

        while (ARRAY[j] > pivot && j > low)
        {
            j--;
        }

        if (i <= j)
        {
            int temp = ARRAY[i];
            ARRAY[i] = ARRAY[j];
            ARRAY[j] = temp;

            i++;
            j--;
        }
    } while (i <= j);

    if (low < j)
    {
        qsort(low, j);
    }
    if (high > i)
    {
        qsort(i, high);
    }
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> ARRAY[i];
    }

    qsort(0, N - 1);

    for (int i = 0; i < N; i++)
    {
        cout << ARRAY[i] << '\n';
    }

    return 0;
}
