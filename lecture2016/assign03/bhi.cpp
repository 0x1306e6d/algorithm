/*
    Black Hole
    Input:
        8
        100 200
        23 90
        55 55
        89 12
        55 57
        57 55
        67 59
        53 61
    Output:
        2
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX 10000
using namespace std;

long long get_dist(int i, int j);
long long BHI(long long d1, long long d2, long long d3);

int N;
pair<int, int> TABLE[MAX];
long long DIST_STORE[MAX][MAX];

int main()
{
    // clock_t start = clock();
    FILE *in, *out;
    in = fopen("bhi.inp", "r");
    out = fopen("bhi.out", "w");
    memset(TABLE, 0, sizeof(TABLE));

    // scanf("%d", &N);
    fscanf(in, "%d", &N);
    for (int i = 0; i < N; ++i)
    {
        int x, y;
        // scanf("%d %d", &x, &y);
        fscanf(in, "%d %d", &x, &y);
        TABLE[i] = make_pair(x, y);
    }

    sort(TABLE, TABLE + N);

    long long min = 9876543210;
    for (int i = 0; i < N; ++i)
    {
        for (int j = i + 1; j < N; ++j)
        {
            long long a = get_dist(i, j);
            if (a > min)
            {
                continue;
            }

            for (int k = j + 1; k < N; ++k)
            {
                long long b = get_dist(j, k);
                long long c = get_dist(i, k);
                long long bhi = BHI(a, b, c);
                if (bhi < min)
                {
                    min = bhi;
                }
            }
        }
    }

    min = sqrt(min);

    // printf("%lld\n", min);
    fprintf(out, "%lld", min);

    // clock_t end = clock();
    // printf("Time : %f", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}

long long get_dist(int i, int j)
{
    if (DIST_STORE[i][j] == 0)
    {
        pair<int, int> p1 = TABLE[i];
        pair<int, int> p2 = TABLE[j];
        long long a = p1.first - p2.first;
        long long b = p1.second - p2.second;
        long long dist = a * a + b * b;

        DIST_STORE[i][j] = dist;
        DIST_STORE[j][i] = dist;
        return dist;
    }
    else
    {
        return DIST_STORE[i][j];
    }
}

long long BHI(long long d1, long long d2, long long d3)
{
    if (d1 > d2)
    {
        return max(d1, d3);
    }
    else
    {
        return max(d2, d3);
    }
}