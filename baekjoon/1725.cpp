/*
    1725 : 히스토그램
    URL : https://www.acmicpc.net/problem/1725
    Input :
        7
        2
        1
        4
        5
        1
        3
        3
    Output :
        8
*/

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <cstring>

#define MAX_N 100001

uint32_t n;
uint32_t heights[MAX_N];

uint64_t biggess(uint32_t start, uint32_t end)
{
    if (start == end)
    {
        return heights[start];
    }

    uint32_t mid = ((start + end) / 2);
    uint64_t surface = 0;

    surface = std::max<uint64_t>(biggess(start, mid), biggess(mid + 1, end));

    uint32_t left = mid;
    uint32_t right = (mid + 1);
    uint32_t height = std::min<uint32_t>(heights[left], heights[right]);
    uint32_t width = 2;
    surface = std::max<uint64_t>(surface, (height * width));
    while ((start < left) || (right < end))
    {
        if ((right < end) &&
            ((left == start) || (heights[left - 1] < heights[right + 1])))
        {
            right++;
            height = std::min<uint32_t>(height, heights[right]);
        }
        else
        {
            left--;
            height = std::min<uint32_t>(height, heights[left]);
        }
        width++;

        surface = std::max<uint64_t>(surface, (height * width));
    }

    return surface;
}

int main(int argc, char const *argv[])
{
    memset(&(heights[0]), 0, sizeof(uint32_t) * MAX_N);

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> heights[i];
    }

    std::cout << biggess(0, n - 1) << std::endl;

    return 0;
}