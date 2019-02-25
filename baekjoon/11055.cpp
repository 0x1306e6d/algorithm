/*
    11055 : 가장 큰 증가 부분 수열
    URL : https://www.acmicpc.net/problem/11055
    Input : 
        10
        1 100 2 50 60 3 5 6 7 8
    Output :
        113
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

int n;
int array[MAX_N];
int cache[MAX_N];

int lcs(int current)
{
    int &ret = cache[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = array[current];
    for (int next = (current + 1); next < n; next++)
    {
        if (array[current] < array[next])
        {
            ret = std::max(ret, array[current] + lcs(next));
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> array[i];
    }

    int max = 0;
    for (int i = 0; i < n; i++)
    {
        max = std::max(max, lcs(i));
    }
    std::cout << max;

    return 0;
}
