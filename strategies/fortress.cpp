/*
    FORTRESS : 요새
    Difficulty : 중
    Input :
        2
        3
        5 5 15
        5 5 10
        5 5 5
        8
        21 15 20
        15 15 10
        13 12 5
        12 12 3
        19 19 2
        30 24 5
        32 10 7
        32 9 4
    Output :
        2
        5
*/

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

#define MAX_N 101

int root = 0;
int subtree = 0;

struct tree
{
    int x;
    int y;
    int r;
    std::vector<struct tree *> children;
};

bool compare(struct tree t1, struct tree t2)
{
    return (t1.r > t2.r);
}

int height(struct tree *root)
{
    std::vector<int> heights;

    for (std::vector<struct tree *>::iterator it = root->children.begin();
         it != root->children.end();
         ++it)
    {
        heights.push_back(height(*it));
    }

    if (heights.empty())
    {
        return 0;
    }

    std::sort(heights.begin(), heights.end());

    if (heights.size() >= 2)
    {
        int nheights = heights.size();
        subtree = std::max(subtree,
                           heights[nheights - 1] + heights[nheights - 2] + 2);
    }
    return heights.back() + 1;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        root = 0;
        subtree = 0;

        struct tree tree[MAX_N];

        int n;
        std::cin >> n;

        for (int i = 0; i < n; i++)
        {
            std::cin >> tree[i].x;
            std::cin >> tree[i].y;
            std::cin >> tree[i].r;
        }

        std::sort(tree, tree + n, compare);

        for (int i = 1; i < n; i++)
        {
            for (int j = (i - 1); j >= 0; j--)
            {
                double xx = std::pow(tree[i].x - tree[j].x, 2);
                double yy = std::pow(tree[i].y - tree[j].y, 2);
                double distance = std::sqrt(xx + yy);
                if (distance < (tree[i].r + tree[j].r))
                {
                    tree[j].children.push_back(&(tree[i]));
                    break;
                }
            }
        }

        root = height(&(tree[0]));
        std::cout << std::max(root, subtree) << std::endl;
    }

    return 0;
}
