/*
    1965 : 상자넣기
    URL : https://www.acmicpc.net/problem/1965
    Input :
        8
        1 6 2 5 7 3 5 6
    Output :
        5
*/

#include <iostream>
#include <cstring>

#define MAX_N 1001

int n;
int boxes[MAX_N];
int cache[MAX_N];

int lis(int i)
{
    int &ret = cache[i];
    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int j = (i + 1); j < n; j++)
    {
        if (boxes[i] < boxes[j])
        {
            ret = std::max(ret, 1 + lis(j));
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    std::memset(&(cache[0]), -1, sizeof(int) * MAX_N);

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> boxes[i];
    }

    int count = 0;
    for (int i = 0; i < n; i++)
    {
        count = std::max(count, lis(i));
    }
    std::cout << count;

    return 0;
}
