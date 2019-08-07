/*
    15596 : 정수 N개의 합
    URL : https://www.acmicpc.net/problem/15596
    Input :
    Output :
*/

#include <vector>

long long sum(std::vector<int> &a)
{
    long long ans = 0;
    for (std::vector<int>::iterator it = a.begin(); it != a.end(); ++it)
    {
        ans += (*it);
    }
    return ans;
}
