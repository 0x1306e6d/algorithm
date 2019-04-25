/*
    6549 : 히스토그램에서 가장 큰 직사각형
    URL : https://www.acmicpc.net/problem/6549
    Input :
        7 2 1 4 5 1 3 3
        4 1000 1000 1000 1000
        0
    Output :
        8
        4000
*/

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <cstring>

#define MAX_N 100001

int n;
int heights[MAX_N];

uint64_t biggesst(int start, int end)
{
    if (start == end)
    {
        return heights[start];
    }

    int mid = ((start + end) / 2);
    uint64_t surface = 0;

    surface = std::max<uint64_t>(biggesst(start, mid), biggesst(mid + 1, end));

    int left = mid;
    int right = (mid + 1);
    int height = std::min<int>(heights[left], heights[right]);
    int width = 2;
    surface = std::max<uint64_t>(surface, 
                                 ((uint64_t) height * (uint64_t) width));
    while ((start < left) || (right < end))
    {
        if ((right < end) &&
            ((left == start) || (heights[left - 1] < heights[right + 1])))
        {
            right++;
            height = std::min<int>(height, heights[right]);
        }
        else
        {
            left--;
            height = std::min<int>(height, heights[left]);
        }
        width++;

        surface = std::max<uint64_t>(surface,
                                     ((uint64_t) height * (uint64_t) width));
    }

    return surface;
}

int main(int argc, char const *argv[])
{
    while (true) {
        memset(&(heights[0]), 0, sizeof(int) * MAX_N);

        std::cin >> n;

        if (n == 0)
        {
            break;
        }

        for (int i = 0; i < n; i++)
        {
            std::cin >> heights[i];
        }

        printf("%lld\n", biggesst(0, n - 1));
    }

    return 0;
}