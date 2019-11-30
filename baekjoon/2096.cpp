/*
    2096 : 내려가기
    URL : https://www.acmicpc.net/problem/2096
    Input :
        3
        1 2 3
        4 5 6
        4 9 0
    Output :
        18 6
*/

#include <iostream>
#include <cstring>

int main(int argc, char const *argv[])
{
    int upperMax[3] = {0, 0, 0};
    int currentMax[3] = {0, 0, 0};

    int upperMin[3] = {0, 0, 0};
    int currentMin[3] = {0, 0, 0};

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a;
        int b;
        int c;
        std::cin >> a;
        std::cin >> b;
        std::cin >> c;

        currentMax[0] = std::max(upperMax[0], upperMax[1]) + a;
        currentMax[1] = std::max(std::max(upperMax[0], upperMax[1]), upperMax[2]) + b;
        currentMax[2] = std::max(upperMax[1], upperMax[2]) + c;

        std::memcpy(&(upperMax[0]), &(currentMax[0]), sizeof(int) * 3);

        currentMin[0] = std::min(upperMin[0], upperMin[1]) + a;
        currentMin[1] = std::min(std::min(upperMin[0], upperMin[1]), upperMin[2]) + b;
        currentMin[2] = std::min(upperMin[1], upperMin[2]) + c;

        std::memcpy(&(upperMin[0]), &(currentMin[0]), sizeof(int) * 3);
    }

    std::cout << std::max(std::max(upperMax[0], upperMax[1]), upperMax[2]);
    std::cout << " ";
    std::cout << std::min(std::min(upperMin[0], upperMin[1]), upperMin[2]);

    return 0;
}
