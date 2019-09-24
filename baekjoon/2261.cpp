/*
    2261 : 가장 가까운 두 점
    URL : https://www.acmicpc.net/problem/2261
    Input :
        4
        0 0
        10 10
        0 10
        10 0
    Output :
        100
*/

#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits>
#include <vector>

struct point
{
    int x;
    int y;
};

bool comp(struct point &a, struct point &b)
{
    return (a.x < b.x);
}

int distance(struct point &a, struct point &b)
{
    return std::pow(a.x - b.x, 2) + std::pow(a.y - b.y, 2);
}

int minDistance(std::vector<struct point> &points, int left, int right)
{

    if (left < right)
    {
        int mid = (left + right) / 2;

        int leftDistance = minDistance(points, left, mid);
        int rightDistance = minDistance(points, mid + 1, right);

        int midDistance = std::numeric_limits<int>::max();
        if (left != mid)
        {
            midDistance = distance(points[left], points[mid]);
        }
        if (mid != right)
        {
            midDistance = std::min(midDistance,
                                   distance(points[mid], points[right]));
        }
        return std::min(leftDistance, std::min(midDistance, rightDistance));
    }
    else
    {
        return std::numeric_limits<int>::max();
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<struct point> points(n);

    for (int i = 0; i < n; i++)
    {
        std::cin >> points[i].x;
        std::cin >> points[i].y;
    }

    std::sort(points.begin(), points.end(), comp);

    std::cout << minDistance(points, 0, n - 1);

    return 0;
}
