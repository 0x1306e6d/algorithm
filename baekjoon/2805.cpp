/*
    2805 : 나무 자르기
    URL : https://www.acmicpc.net/problem/2805
    Input :
        4 7
        20 15 10 17
    Output :
        15
*/
#include <iostream>
#include <cstring>

#define MAX_N 1000001
#define MIN_M 0

using namespace std;

int N;
int M;
long long MAX = MIN_M;
int TREE[MAX_N];

int main(int argc, char const *argv[])
{
    cin >> N;
    cin >> M;

    for (int i = 0; i < N; i++)
    {
        cin >> TREE[i];

        if (TREE[i] > MAX)
        {
            MAX = TREE[i];
        }
    }

    long long start = 0;
    long long end = MAX;
    long long result = 0;
    while (start <= end)
    {
        long long current = (start + end) / 2;

        long long length = 0;
        for (int i = 0; i < N; i++)
        {
            if (current < TREE[i])
            {
                length += TREE[i] - current;
            }
        }

        if (length >= M)
        {
            if (current > result)
            {
                result = current;
            }
            start = current + 1;
        }
        else if (length < M)
        {
            end = current - 1;
        }
    }

    cout << result;

    return 0;
}
