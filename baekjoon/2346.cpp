/*
    2346 : 풍선 터뜨리기
    URL : https://www.acmicpc.net/problem/2346
    Input :
        5
        3 2 1 -3 -1
    Output :
        1 4 5 3 2
*/

#include <iostream>

struct node
{
    int index;
    int value;
    struct node *pLeft;
    struct node *pRight;
};

int main(int argc, char const *argv[])
{
    struct node *pBegin = NULL;
    struct node *pEnd = NULL;
    struct node *pCursor = NULL;

    int n;
    std::cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int value;
        std::cin >> value;

        struct node *pNode = new struct node;
        pNode->index = i;
        pNode->value = value;
        pNode->pLeft = NULL;
        pNode->pRight = NULL;

        if (pBegin == NULL)
        {
            pBegin = pNode;
        }
        else
        {
            pNode->pLeft = pCursor;
            pNode->pRight = pCursor->pRight;

            if (pCursor->pRight == NULL)
            {
                pEnd = pNode;
            }
            else
            {
                pCursor->pRight->pLeft = pNode;
            }
            pCursor->pRight = pNode;
        }

        pCursor = pNode;
    }

    pBegin->pLeft = pEnd;
    pEnd->pRight = pBegin;

    pCursor = pBegin;
    while (n--)
    {
        const int index = pCursor->index;
        const int value = pCursor->value;
        std::cout << index << " ";

        pCursor->pLeft->pRight = pCursor->pRight;
        pCursor->pRight->pLeft = pCursor->pLeft;

        if (value > 0)
        {
            for (int i = 0; i < value; i++)
            {
                pCursor = pCursor->pRight;
            }
        }
        else
        {
            for (int i = 0; i < (-value); i++)
            {
                pCursor = pCursor->pLeft;
            }
        }
    }

    return 0;
}
