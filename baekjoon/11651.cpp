/*
    11651 : 좌표 정렬하기 2
    URL : https://www.acmicpc.net/problem/11651
    Input :
        5
        0 4
        1 2
        1 -1
        2 2
        3 3
    Output :
        1 -1
        1 2
        2 2
        3 3
        0 4
*/

#include <iostream>
#include <vector>

struct point
{
    int x;
    int y;
};

std::vector<struct point> temp;
std::vector<struct point> points;

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while ((i <= mid) && (j <= right))
    {
        if (points[i].y < points[j].y)
        {
            temp[k] = points[i];
            i++;
        }
        else if (points[i].y == points[j].y)
        {
            if (points[i].x < points[j].x)
            {
                temp[k] = points[i];
                i++;
            }
            else
            {
                temp[k] = points[j];
                j++;
            }
        }
        else
        {
            temp[k] = points[j];
            j++;
        }
        k++;
    }

    if (i > mid)
    {
        for (int l = j; l <= right; l++)
        {
            temp[k] = points[l];
            k++;
        }
    }
    else
    {
        for (int l = i; l <= mid; l++)
        {
            temp[k] = points[l];
            k++;
        }
    }

    for (int l = left; l <= right; l++)
    {
        points[l] = temp[l];
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
    int n;
    scanf("%d", &n);

    temp = std::vector<struct point>(n);
    points = std::vector<struct point>(n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &(points[i].x), &(points[i].y));
    }

    msort(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("%d %d\n", points[i].x, points[i].y);
    }

    return 0;
}
