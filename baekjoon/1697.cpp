/*
    1697: 숨바꼭질
    URL: https://www.acmicpc.net/problem/1697
    Input #1:
        5 17
    Output #1:
        4
*/

#include <iostream>
#include <queue>

#define MIN 0
#define MAX 100000

bool visited[MAX + 1];

int main(int argc, char const *argv[])
{
    std::queue<int> q;

    int n;
    int k;
    std::cin >> n;
    std::cin >> k;

    visited[n] = true;
    q.push(n);

    int time = 0;
    while (true)
    {
        bool find = false;
        const size_t size = q.size();
        for (int i = 0; i < size; i++)
        {
            int x = q.front();
            q.pop();

            if (x == k)
            {
                find = true;
                break;
            }
            else
            {
                if (((x - 1) >= MIN) && !visited[x - 1])
                {
                    visited[x - 1] = true;
                    q.push(x - 1);
                }
                if (((x + 1) <= MAX) && !visited[x + 1])
                {
                    visited[x + 1] = true;
                    q.push(x + 1);
                }
                if (((2 * x) <= MAX) && !visited[2 * x])
                {
                    visited[2 * x] = true;
                    q.push(2 * x);
                }
            }
        }

        if (find)
        {
            break;
        }
        else
        {
            time++;
        }
    }

    std::cout << time;

    return 0;
}
