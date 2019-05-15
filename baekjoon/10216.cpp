/*
    10216 : Count Circle Groups
    URL : https://www.acmicpc.net/problem/10216
    Input :
        2
        2
        0 0 1
        1 0 1
        3
        0 0 1
        2 0 1
        10 0 5
    Output :
        1
        2
*/

#include <iostream>
#include <queue>
#include <vector>

struct tower
{
    int x;
    int y;
    int r;
};

bool disjoint(const struct tower &t1, const struct tower &t2)
{
    int xx = (t1.x - t2.x);
    int yy = (t1.y - t2.y);
    int rr = (t1.r + t2.r);
    return ((xx * xx) + (yy * yy)) > (rr * rr);
}

void bfs(int i,
         std::vector<std::vector<int>> &links,
         std::vector<bool> &visited)
{
    std::queue<int> q;
    q.push(i);

    while (!q.empty())
    {
        int j = q.front();
        q.pop();

        int nlink = links[j].size();
        for (int k = 0; k < nlink; k++)
        {
            if (!visited[links[j][k]])
            {
                visited[links[j][k]] = true;
                q.push(links[j][k]);
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        int n;
        std::cin >> n;

        std::vector<struct tower> towers;
        std::vector<std::vector<int>> links(n, std::vector<int>());
        std::vector<bool> visited(n, false);

        for (int i = 0; i < n; i++)
        {
            int x;
            int y;
            int r;
            std::cin >> x;
            std::cin >> y;
            std::cin >> r;

            struct tower t = {x, y, r};
            for (int j = 0; j < towers.size(); j++)
            {
                if (!disjoint(t, towers[j]))
                {
                    links[i].push_back(j);
                    links[j].push_back(i);
                }
            }
            towers.push_back(t);
        }

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                count++;
                visited[i] = true;
                bfs(i, links, visited);
            }
        }
        std::cout << count << std::endl;
    }

    return 0;
}
