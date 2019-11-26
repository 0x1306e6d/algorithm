/*
    5397 : 키로거
    URL : https://www.acmicpc.net/problem/5397
    Input :
        2
        <<BP<A>>Cd-
        ThIsIsS3Cr3t
    Output :
        BAPC
        ThIsIsS3Cr3t
*/

#include <iostream>

struct node
{
    char c;
    struct node *left;
    struct node *right;
};

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    while (n--)
    {
        struct node *cursor = NULL;

        std::string s;
        std::cin >> s;

        for (std::string::iterator it = s.begin(); it != s.end(); ++it)
        {
            switch (*it)
            {
            case '-':
            {
                if (cursor == NULL)
                {
                    break;
                }
                if (cursor->left == NULL)
                {
                    break;
                }

                cursor->left->right = cursor->right;
                if (cursor->right != NULL)
                {
                    cursor->right->left = cursor->left;
                }

                cursor = cursor->left;

                break;
            }
            case '<':
            {
                if (cursor == NULL)
                {
                    break;
                }
                if (cursor->left == NULL)
                {
                    break;
                }

                cursor = cursor->left;

                break;
            }
            case '>':
            {
                if (cursor == NULL)
                {
                    break;
                }
                if (cursor->right == NULL)
                {
                    break;
                }

                cursor = cursor->right;

                break;
            }
            default:
            {
                struct node *n = new struct node;
                n->c = *it;

                if (cursor == NULL)
                {
                    n->left = NULL;
                    n->right = NULL;
                }
                else
                {
                    n->left = cursor;
                    n->right = cursor->right;

                    if (cursor->right != NULL)
                    {
                        cursor->right->left = n;
                    }
                    cursor->right = n;
                }

                cursor = n;

                break;
            }
            }
        }

        while (cursor->left != NULL)
        {
            cursor = cursor->left;
        }

        while (cursor != NULL)
        {
            std::cout << cursor->c;

            cursor = cursor->right;
        }
        std::cout << std::endl;
    }

    return 0;
}

