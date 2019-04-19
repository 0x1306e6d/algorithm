/*
    FENCE : 울타리 잘라내기
    Difficulty : 중
    Input :
        3
        7
        7 1 5 9 6 7 3
        7
        1 4 4 4 4 1 1
        4
        1 8 2 2
    Output :
        20
        16
        8
*/

#include <iostream>
#include <cstring>

#define MAX_N 20000

int n;
int heights[MAX_N];

int fence(int start, int end)
{
    if (start == end)
    {
        return heights[start];
    }

    int mid = ((start + end) / 2);
    int surface = 0;

    surface = std::max(fence(start, mid), fence(mid + 1, end));

    int left = (mid - 1);
    int right = (mid + 1);
    int height = heights[mid];
    int width = 1;
    while ((left >= start) && (right <= end))
    {
        if (heights[left] < heights[right])
        {
            height = std::min(height, heights[right]);
            right++;
        }
        else
        {
            height = std::min(height, heights[left]);
            left--;
        }
        width++;

        surface = std::max(surface, (height * width));
    }

    return surface;
}

int main(int argc, char const *argv[])
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        memset(&(heights[0]), 0, sizeof(int) * MAX_N);

        std::cin >> n;

        for (int i = 0; i < n; i++)
        {
            std::cin >> heights[i];
        }

        std::cout << fence(0, n - 1) << std::endl;
    }

    return 0;
}