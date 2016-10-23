/*
    2331 : 반복수열
    URL : https://www.acmicpc.net/problem/2331
    Input :
        57 2
    Output :
        4
*/
#include <iostream>
#include <vector>
#include <set>
#include <math.h>

#define MAX 10000
using namespace std;

long long parse(int index);

int P;
vector<long long> D;
set<long long> SEARCH;

int main()
{
    int A;
    scanf("%d %d", &A, &P);

    D.push_back(A);
    SEARCH.insert(A);

    for (int i = 1; ; ++i)
    {
        long long p = parse(i);
        D.push_back(p)

        if (SEARCH.find(p) == SEARCH.end())
        {
            SEARCH.insert(p);
        }
        else
        {
            int j;
            for (j = i - 1; j >= 0; --j)
            {
                if (p == D[j])
                {
                    printf("%d", j);
                    break;
                }
            }
            break;
        }
    }
    return 0;
}

long long parse(int index)
{
    long long value = 0;
    long long base = D[index - 1];

    while ((base / 10) > 0)
    {
        int i = base % 10;
        base = base / 10;

        value += pow(i, P);
    }
    value += pow(base, P);

    return value;
}