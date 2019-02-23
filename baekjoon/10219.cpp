/*
    10219 : Meats On The Grill
    URL : https://www.acmicpc.net/problem/10219
    Input :
        1
        3 4
        abbb
        aabb
        aa..
    Output :
        .abb
        aabb
        aa.b
*/

#include <iostream>

#define MAX_H 12
#define MAX_W 12

int main(int argc, char const *argv[])
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        char grill[MAX_H][MAX_W];

        int height;
        int width;
        std::cin >> height;
        std::cin >> width;

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                std::cin >> grill[i][j];
            }
        }

        for (int i = 0; i < height; i++)
        {
            for (int j = (width - 1); j >= 0; j--)
            {
                std::cout << grill[i][j];
            }
            std::cout << std::endl;
        }
    }

    return 0;
}
