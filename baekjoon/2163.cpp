/*
    2163: 초콜릿 자르기
    URL: https://www.acmicpc.net/problem/2163
    Input:
        2 2
    Output:
        3
*/

#include <iostream>

int main(int argc, char const *argv[])
{
    int n;
    int m;
    std::cin >> n;
    std::cin >> m;

    std::cout << (n - 1) + (n * (m - 1));

    return 0;
}
