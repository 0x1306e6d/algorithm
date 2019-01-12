/*
    JLIS : 합친 LIS
    Difficulty : 하
    Input :
        3
        3 3
        1 2 4
        3 4 7
        3 3
        1 2 3
        4 5 6
        5 3
        10 20 30 1 2
        10 20 30
    Output :
        5
        6
        5
*/
#include <iostream>
#include <limits>
#include <cstring>

#define MAX_N 101

using namespace std;

const long long NEGINF = numeric_limits<long long>::min();
int A[MAX_N];
int B[MAX_N];
int cache[MAX_N][MAX_N];

int jlis(int n, int m, int indexA, int indexB)
{
    int &ret = cache[indexA + 1][indexB + 1];

    if (ret != -1)
    {
        return ret;
    }

    ret = 2;
    long long a = (indexA == -1) ? NEGINF : A[indexA];
    long long b = (indexB == -1) ? NEGINF : B[indexB];
    long long maxElement = max(a, b);

    for (int nextA = indexA + 1; nextA < n; nextA++)
    {
        if (maxElement < A[nextA])
        {
            ret = max(ret, jlis(n, m, nextA, indexB) + 1);
        }
    }

    for (int nextB = indexB + 1; nextB < m; nextB++)
    {
        if (maxElement < B[nextB])
        {
            ret = max(ret, jlis(n, m, indexA, nextB) + 1);
        }
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    int c;

    cin >> c;

    for (int i = 0; i < c; i++)
    {
        int n;
        int m;

        memset(&(A[0]), 0, sizeof(int) * MAX_N);
        memset(&(B[0]), 0, sizeof(int) * MAX_N);
        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

        cin >> n;
        cin >> m;

        for (int j = 0; j < n; j++)
        {
            int number;

            cin >> number;

            A[j] = number;
        }

        for (int j = 0; j < m; j++)
        {
            int number;

            cin >> number;

            B[j] = number;
        }

        cout << (jlis(n, m, -1, -1) - 2) << endl;
    }

    return 0;
}
