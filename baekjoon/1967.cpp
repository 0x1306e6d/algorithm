/*
    1967 : 트리의 지름
    URL : https://www.acmicpc.net/problem/1967
    Input :
        12
        1 2 3
        1 3 2
        2 4 5
        3 5 11
        3 6 9
        4 7 1
        4 8 7
        5 9 15
        5 10 4
        6 11 6
        6 12 10
    Output :
        45
*/

#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_N 10001

int subtree = 0;

struct tree
{
    std::vector<std::pair<struct tree *, int>> children;
};

int height(struct tree *root)
{
    std::vector<int> heights;
    std::vector<std::pair<struct tree *, int>>::iterator it;

    for (it = root->children.begin(); it != root->children.end(); ++it)
    {
        std::pair<struct tree *, int> p = *it;
        heights.push_back(p.second + height(p.first));
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
    struct tree tree[MAX_N];

    int n;
    std::cin >> n;

    for (int i = 0; i < (n - 1); i++)
    {
        int p;
        int c;
        int w;
        std::cin >> p;
        std::cin >> c;
        std::cin >> w;

        tree[p].children.push_back(std::make_pair(&(tree[c]), w));
    }

    int root = height(&(tree[1]));
    std::cout << std::max(root, subtree);

    return 0;
}
