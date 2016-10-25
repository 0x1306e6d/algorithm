/*
assign02 : 삼총수
Input:
9
16 12
7 11
68 33
7 6
8 11
17 63
9 8
2 3
31 55
Output:
5 1 3
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
// #include <time.h>

#define MAX 100000

using namespace std;

typedef struct
{
	int index;
	int p;
	int q;
} FRACTION;

bool compare(FRACTION* f1, FRACTION* f2);
FRACTION* add(FRACTION* f1, FRACTION* f2);
int subtract(FRACTION* f1, FRACTION* f2);
long long subtract_ll(FRACTION* f1, FRACTION* f2);
int search(FRACTION* f);

int T;
FRACTION* TABLE[MAX];
FRACTION* SORTED[MAX];

int main()
{
    // clock_t begin, end;
    // begin = clock();
    FILE *in, *out;
    in = fopen("trio.inp", "r");
    out = fopen("trio.out", "w");

    int i, j;
    int p, q;
    int index;
    FRACTION* f;
    FRACTION* a;
    FRACTION* b;
    FRACTION* left;
    fscanf(in, "%d", &T);
	for (i = 0; i < T; ++i)
	{
        fscanf(in, "%d %d", &p, &q);
		FRACTION* f = new FRACTION;
		f->index = i;
		f->p = p;
		f->q = q;
        TABLE[i] = f;
        SORTED[i] = f;
	}

	sort(SORTED, SORTED + T, compare);

    int limit1 = T - 2;
    int limit2 = T - 1;
	for (i = 0; i < limit1; ++i)
	{
		a = TABLE[i];
		for (j = 0; j < limit2; ++j)
		{
			if (i == j)
			{
				continue;
			}
			b = TABLE[j];
			if (subtract(a, b) <= 0)
            {
				left = add(a, b);
                index = search(left);
                if (index != -1)
                {
                    fprintf(out, "%d %d %d", (i + 1), (j + 1), (index + 1));
                    // end = clock();
                    // cout << "수행시간 : " << (end - begin) << endl;
                    return 0;
                }
			}
		}
	}
    fprintf(out, "0 0 0");
    // end = clock();
    // cout << "수행시간 : " << (end - begin) << endl;
	return 0;
}

// return true when f1 <= f2
bool compare(FRACTION* f1, FRACTION* f2)
{
    return (f1->p * f2->q) < (f2->p * f1->q);
}

// return f1 + f2
FRACTION* add(FRACTION* f1, FRACTION* f2)
{
	FRACTION* f = new FRACTION;
	f->p = f1->p * f2->q + f2->p * f1->q;
	f->q = f1->q * f2->q;
	return f;
}

// return f1 - f2
int subtract(FRACTION* f1, FRACTION* f2)
{
    return f1->p * f2->q - f2->p * f1->q;
}

// return f1 - f2
long long subtract_ll(FRACTION* f1, FRACTION* f2)
{
	return (long long) f1->p * f2->q - (long long) f2->p * f1->q;
}

int search(FRACTION* f)
{
    int low = 2;
    int high = T - 1;
    int mid;
    long long s;
    while (low <= high)
    {
        mid = (low + high) / 2;
        s = subtract_ll(SORTED[mid], f);
        if (s > 0)
            high = mid - 1;
        else if (s < 0)
            low = mid + 1;
        else
            return SORTED[mid]->index;
    }
    return -1;
}