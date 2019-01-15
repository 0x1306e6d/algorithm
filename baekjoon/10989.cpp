/*
    10989 : 수 정렬하기 3
    URL : https://www.acmicpc.net/problem/10989
    Input :
        10
        5
        2
        3
        1
        4
        2
        3
        5
        1
        7
    Output :
        1
        1
        2
        2
        3
        3
        4
        5
        5
        7
*/
#include <iostream>
#include <cstring>

#define MAX_NUMBER 10001

using namespace std;

uint32_t cache[MAX_NUMBER];

int main(int argc, char const *argv[])
{
    int N;

    ios::sync_with_stdio(false);

    memset(&(cache[0]), 0, sizeof(uint32_t) * MAX_NUMBER);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int number;

        cin >> number;

        cache[number] += 1;
    }

    for (int i = 0; i < MAX_NUMBER; i++)
    {
        if (cache[i] != 0)
        {
            for (int j = 0; j < cache[i]; j++)
            {
                cout << i << '\n';
            }
        }
    }

    return 0;
}
