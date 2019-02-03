/*
    9251 : LCS
    URL : https://www.acmicpc.net/problem/9251
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
int CACHE[MAX_N][MAX_N];

int LCS(int a, int b)
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
        ret = 1 + LCS(a + 1, b + 1);
    }
    else
    {
        ret = max(LCS(a + 1, b), LCS(a, b + 1));
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(CACHE[0][0]), -1, sizeof(int) * MAX_N * MAX_N);

    cin >> A;
    cin >> B;

    cout << LCS(0, 0);

    return 0;
}
