/*
    17951: 흩날리는 시험지 속에서 내 평점이 느껴진거야
    URL: https://www.acmicpc.net/problem/17951
    Input:
        8 2
        12 7 19 20 17 14 9 10
    Output:
        50
*/

#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_N 100001

int scores[MAX_N];

int main(int argc, char const *argv[])
{
    int n;
    int k;
    std::cin >> n;
    std::cin >> k;

    for (int i = 0; i < n; i++)
    {
        std::cin >> scores[i];
    }

    std::vector<int> combination;
    for (int i = 0; i < (n - k + 1); i++)
    {
        combination.push_back(0);
    }
    for (int i = 0; i < (k - 1); i++)
    {
        combination.push_back(1);
    }

    int maxSum = 0;
    do
    {
        int minSum = 987654321;
        int sum = 0;
        for (int i = 0; i < combination.size(); i++)
        {
            sum += scores[i];

            if (combination[i] == 1)
            {
                minSum = std::min(minSum, sum);
                sum = 0;
            }
        }
        minSum = std::min(minSum, sum);
        maxSum = std::max(maxSum, minSum);
    } while (std::next_permutation(combination.begin(), combination.end()));

    std::cout << maxSum;

    return 0;
}
