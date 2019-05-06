/*
    1167 : 트리의 지름
    URL : https://www.acmicpc.net/problem/1167
    Input :
        5
        1 3 2 -1
        2 4 4 -1
        3 1 2 4 3 -1
        4 2 4 3 3 5 6 -1
        5 4 6 -1
    Output :
        11
*/

#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_V 100001

int subtree = 0;

struct tree
{
    bool visited;
    std::vector<std::pair<struct tree *, int>> children;
};

int height(struct tree *root)
{
    std::vector<int> heights;
    std::vector<std::pair<struct tree *, int>>::iterator it;

    root->visited = true;

    for (it = root->children.begin(); it != root->children.end(); ++it)
    {
        std::pair<struct tree *, int> p = *it;
        if (!(p.first->visited))
        {
            heights.push_back(p.second + height(p.first));
        }
    }

    if (heights.empty())
    {
        return 0;
    }

    int nheights = heights.size();
    if (nheights >= 2)
    {
        std::sort(heights.begin(), heights.end());

        subtree = std::max(subtree,
                           heights[nheights - 2] + heights[nheights - 1]);
    }
    return heights.back();
}

int main(int argc, char const *argv[])
{
    struct tree tree[MAX_V];

    int V;
    std::cin >> V;

    for (int v = 0; v < V; v++)
    {
        int n;
        std::cin >> n;

        int m;
        int distance;
        while (true)
        {
            std::cin >> m;
            if (m == -1)
            {
                break;
            }

            std::cin >> distance;
            tree[n].children.push_back(std::make_pair(&(tree[m]), distance));
            tree[m].children.push_back(std::make_pair(&(tree[n]), distance));
        }
    }

    int root = height(&(tree[1]));
    std::cout << std::max(root, subtree);

    return 0;
}
