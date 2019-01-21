/*
    11053 : 가장 긴 증가하는 부분 수열
    URL : https://www.acmicpc.net/problem/11053
    Input : 
        6
        10 20 10 30 20 50
    Output :
        4
*/
#include <iostream>
#include <cstring>

#define MAX_N 1001

using namespace std;

int N;
int A[MAX_N];

int cache[MAX_N];

int lis(int current)
{
    int &ret = cache[current + 1];

    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int next = current + 1; next < N; next++)
    {
        if (current == -1 || A[current] < A[next])
        {
            ret = max(ret, lis(next) + 1);
        }
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(A[0]), 0, sizeof(int) * MAX_N);
    memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    cout << (lis(-1) - 1);

    return 0;
}
