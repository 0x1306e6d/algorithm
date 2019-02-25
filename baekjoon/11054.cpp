/*
    11054 : 가장 긴 바이토닉 부분 수열
    URL : https://www.acmicpc.net/problem/11054
    Input : 
        10
        1 5 2 1 4 3 4 5 2 1
    Output :
        7
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

int n;
int array[MAX_N];
int cache[MAX_N];
int ldsCache[MAX_N];

int lds(int current)
{
    int &ret = ldsCache[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int next = (current + 1); next < n; next++)
    {
        if (array[current] > array[next])
        {
            ret = std::max(ret, lds(next) + 1);
        }
    }
    return ret;
}

int bitonic(int current)
{
    int &ret = cache[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = lds(current);
    for (int next = (current + 1); next < n; next++)
    {
        if (array[current] < array[next])
        {
            ret = std::max(ret, bitonic(next) + 1);
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    memset(&(cache[0]), -1, sizeof(int) * MAX_N);
    memset(&(ldsCache[0]), -1, sizeof(int) * MAX_N);

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> array[i];
    }

    int count = 0;
    for (int i = 0; i < n; i++)
    {
        count = std::max(count, bitonic(i));
    }
    std::cout << count;

    return 0;
}
