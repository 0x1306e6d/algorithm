/*
    15678 : 연세워터파크
    URL : https://www.acmicpc.net/problem/15678
    Input #1 :
        10 2
        2 7 -5 -4 10 -5 -5 -5 30 -10
    Output #1 :
        40
    Input #2 :
        3 2
        -4 -2 -7
    Output #2 :
        -2
*/

#include <iostream>
#include <cstdint>
#include <cstring>
#include <queue>

#define MAX_N 100001

int n;
int d;
int64_t stones[MAX_N];

int main(int argc, char const *argv[])
{
    std::cin >> n;
    std::cin >> d;

    for (int i = 0; i < n; i++)
    {
        std::cin >> stones[i];
    }

    int64_t answer = stones[0];
    std::priority_queue<std::pair<int64_t, int>> pq;
    pq.push(std::make_pair(stones[0], 0));
    for (int i = 1; i < n; i++)
    {
        while (!pq.empty())
        {
            std::pair<int64_t, int> item = pq.top();

            if (item.second < (i - d))
            {
                pq.pop();
                continue;
            }

            int64_t here = std::max(stones[i], stones[i] + item.first);
            answer = std::max(answer, here);
            pq.push(std::make_pair(here, i));
            break;
        }
    }

    std::cout << answer;

    return 0;
}
