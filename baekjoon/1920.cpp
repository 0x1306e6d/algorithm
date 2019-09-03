/*
    1920 : 수 찾기
    URL : https://www.acmicpc.net/problem/1920
    Input :
        5
        4 1 5 2 3
        5
        1 3 7 9 5
    Output :
        1
        1
        0
        0
        1
*/

#include <cstdio>

#define MAX_N 100001

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

bool bsearch(int left, int right, int n)
{
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (a[mid] == n)
        {
            return true;
        }
        else if (a[mid] < n)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return false;
}

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &(a[i]));
    }

    msort(0, n - 1);

    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        int j;
        scanf("%d", &j);

        if (bsearch(0, n - 1, j))
        {
            printf("1\n");
        }
        else
        {
            printf("0\n");
        }
    }

    return 0;
}
