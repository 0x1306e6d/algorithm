/*
    1201 : NMK
    URL : https://www.acmicpc.net/problem/1201
    Input :
        4 2 2
    Output :
        2 1 4 3
*/

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

#define MAX_N 501

int n;
int m;
int k;

std::vector<int> permutation;
int dp[MAX_N];

int lis(int current)
{
    int &ret = dp[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int next = (current + 1); next < n; next++)
    {
        if (permutation[next] > permutation[current])
        {
            ret = std::max(ret, lis(next) + 1);
        }
    }
    return ret;
}

int lds(int current)
{
    int &ret = dp[current];
    if (ret != -1)
    {
        return ret;
    }

    ret = 1;
    for (int next = (current + 1); next < n; next++)
    {
        if (permutation[current] > permutation[next])
        {
            ret = std::max(ret, lds(next) + 1);
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> m;
    std::cin >> k;

    for (int i = 1; i <= n; i++)
    {
        permutation.push_back(i);
    }

    bool found = false;
    do
    {
        std::memset(&(dp[0]), -1, sizeof(int) * MAX_N);
        int lisCount = 0;
        for (int i = 0; i < n; i++)
        {
            lisCount = std::max(lisCount, lis(i));
        }

        if (lisCount == m)
        {
            std::cout << "과연?" << std::endl;
            std::memset(&(dp[0]), -1, sizeof(int) * MAX_N);
            int ldsCount = 0;
            for (int i = 0; i < n; i++)
            {
                ldsCount = std::max(ldsCount, lds(i));
            }

            if (ldsCount == k)
            {
                found = true;
                break;
            }
        }
    } while (std::next_permutation(permutation.begin(), permutation.end()));

    if (found)
    {
        for (int i = 0; i < n; i++)
        {
            std::cout << permutation[i];

            if (i < (n - 1))
            {
                std::cout << " ";
            }
        }
    }
    else
    {
        std::cout << -1;
    }

    return 0;
}
