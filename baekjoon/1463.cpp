/*
    1463 : 1로 만들기
    URL : https://www.acmicpc.net/problem/1463
    Input #1 :
        2
    Output #1 :
        1
    Input #2 :
        10
    Output #2 :
        3
*/
#include <iostream>
#include <limits>
#include <cstring>

#define MAX_N 1000001

using namespace std;

const int POSINF = numeric_limits<int>::max();

int cache[MAX_N];

int one(int N)
{
    int &ret = cache[N];

    if (ret != -1)
    {
        return ret;
    }

    ret = POSINF;

    // X가 3으로 나누어 떨어지면, 3으로 나눈다.
    if ((N % 3) == 0)
    {
        ret = min(ret, one(N / 3) + 1);
    }

    // X가 2로 나누어 떨어지면, 2로 나눈다.
    if ((N % 2) == 0)
    {
        ret = min(ret, one(N / 2) + 1);
    }

    // 1을 뺀다.
    ret = min(ret, one(N - 1) + 1);

    return ret;
}

int main(int argc, char const *argv[])
{
    int N;

    memset(&(cache[0]), -1, sizeof(int) * MAX_N);
    cache[0] = 0;
    cache[1] = 0;

    cin >> N;
    cout << one(N);

    return 0;
}