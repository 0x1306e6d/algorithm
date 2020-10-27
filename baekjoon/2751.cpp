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

int n;
int a[MAX_N];
int temp[MAX_N];

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while ((i <= mid) && (j <= right))
    {
        if (a[i] < a[j])
        {
            temp[k] = a[i];
            i++;
        }
        else
        {
            temp[k] = a[j];
            j++;
        }
        k++;
    }

    if (i > mid)
    {
        for (int l = j; l <= right; l++)
        {
            temp[k] = a[l];
            k++;
        }
    }
    else
    {
        for (int l = i; l <= mid; l++)
        {
            temp[k] = a[l];
            k++;
        }
    }

    for (int l = left; l <= right; l++)
    {
        a[l] = temp[l];
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
    ios::sync_with_stdio(false);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    msort(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << '\n';
    }

    return 0;
}
