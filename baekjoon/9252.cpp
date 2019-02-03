/*
    9252 : LCS 2
    URL : https://www.acmicpc.net/problem/9252
    Input :
        ACAYKP
        CAPCAK
    Output :
        4
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

using namespace std;

string A;
string B;
string LCS;
int CACHE[MAX_N][MAX_N];

int lcslen(int a, int b)
{
    if ((a == A.size()) || (b == B.size()))
    {
        return 0;
    }

    int &ret = CACHE[a][b];

    if (ret != -1)
    {
        return ret;
    }

    if (A[a] == B[b])
    {
        ret = 1 + lcslen(a + 1, b + 1);
    }
    else
    {
        ret = max(lcslen(a + 1, b), lcslen(a, b + 1));
    }
    return ret;
}

void mklcs(int a, int b)
{
    if ((a == A.size()) || (b == B.size()))
    {
        return;
    }

    if (A[a] == B[b])
    {
        LCS.push_back(A[a]);
        mklcs(a + 1, b + 1);
    }
    else
    {
        if (CACHE[a + 1][b] >= CACHE[a][b + 1])
        {
            mklcs(a + 1, b);
        }
        else
        {
            mklcs(a, b + 1);
        }
    }
}

int main(int argc, char const *argv[])
{
    memset(&(CACHE[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

    cin >> A;
    cin >> B;

    cout << lcslen(0, 0) << endl;

    mklcs(0, 0);
    cout << LCS;

    return 0;
}
