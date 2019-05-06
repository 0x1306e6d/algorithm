/*
    TRAVERSAL : 트리 순회 순서 변경
    Difficulty : 하
    Input :
        2
        7
        27 16 9 12 54 36 72
        9 12 16 27 36 54 72
        6
        409 479 10 838 150 441
        409 10 479 150 838 441
    Output :
        12 9 16 36 72 54 27
        10 150 441 838 479 409
*/

#include <iostream>

#define MAX_N 101

int preorder[MAX_N];
int inorder[MAX_N];

void traverse(int preLow, int preHigh, int inLow, int inHigh)
{
    if ((preLow <= preHigh) && (inLow <= inHigh))
    {
        int root = preorder[preLow];

        int pivot = 0;
        for (pivot; inorder[pivot] != root; pivot++)
            ;
        int nLeft = pivot - inLow;
        int nRight = inHigh - pivot;

        traverse(preLow + 1, preLow + nLeft, inLow, inLow + nLeft - 1);
        traverse(preHigh - nRight + 1, preHigh, inHigh - nRight + 1, inHigh);

        printf("%d ", root);
    }
}

int main(int argc, char const *argv[])
{
    int C;
    scanf("%d", &C);

    for (int c = 0; c < C; c++)
    {
        int n;
        scanf("%d", &n);

        for (int i = 0; i < n; i++)
        {
            scanf("%d", &preorder[i]);
        }
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &inorder[i]);
        }

        traverse(0, n - 1, 0, n - 1);
        printf("\n");
    }

    return 0;
}
