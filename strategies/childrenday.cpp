/*
    CHILDRENDAY : 어린이날
    Difficulty : 상
    Input :
        5
        1 7 0
        1 10 1 
        0 7 3
        345 9997 3333
        35 9 8
    Output :
        111111
        11
        IMPOSSIBLE
        35355353545
        35
*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>

int append(int here, int edge, int mod)
{
    int there = (here * 10) + edge;
    if (there >= mod)
    {
        return mod + (there % mod);
    }
    else
    {
        return there % mod;
    }
}

std::string childrenday(std::string &d, int n, int m)
{
    std::sort(d.begin(), d.end());

    std::vector<int> vertices(2 * n, -1);
    std::vector<int> weights(2 * n, -1);
    std::queue<int> q;

    vertices[0] = 0;
    q.push(0);
    while (!q.empty())
    {
        int here = q.front();
        q.pop();

        for (int i = 0; i < d.size(); i++)
        {
            int there = append(here, d[i] - '0', n);
            if (vertices[there] == -1)
            {
                vertices[there] = here;
                weights[there] = (d[i] - '0');
                q.push(there);
            }
        }
    }

    if (vertices[n + m] == -1)
    {
        return "IMPOSSIBLE";
    }

    std::string gift;
    int here = n + m;
    while (vertices[here] != here)
    {
        gift += char('0' + weights[here]);
        here = vertices[here];
    }
    std::reverse(gift.begin(), gift.end());
    return gift;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        std::string d;
        int n;
        int m;
        std::cin >> d;
        std::cin >> n;
        std::cin >> m;

        std::cout << childrenday(d, n, m) << std::endl;
    }

    return 0;
}
