/*
    11722 : 가장 긴 감소하는 부분 수열
    URL : https://www.acmicpc.net/problem/11722
    Input :
        6
        10 30 10 20 20 10
    Output :
        3
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

int n;
int array[MAX_N];
int cache[MAX_N];

int lds(int current)
{
    int &ret = cache[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int next = (current + 1); next < n; next++)
    {
        if (array[current] > array[next])
        {
            ret = std::max(ret, 1 + lds(next));
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

    int count = 0;
    for (int i = 0; i < n; i++)
    {
        count = std::max(count, lds(i));
    }
    std::cout << count;

    return 0;
}
