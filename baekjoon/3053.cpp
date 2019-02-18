/*
    3053 : 택시 기하학
    URL : https://www.acmicpc.net/problem/3053
    Input :
        1
    Output :
        3.141593
        2.000000
*/

#include <iostream>

#define PI 3.1415926535897932

int main(int argc, char const *argv[])
{
    int R;

    std::cin >> R;

    std::cout << std::fixed;
    std::cout.precision(6);

    std::cout << R * R * PI << std::endl;
    std::cout << R * R * 2.0 << std::endl;

    return 0;
}