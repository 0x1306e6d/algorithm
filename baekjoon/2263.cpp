/*
    2263 : 트리의 순회
    URL : https://www.acmicpc.net/problem/2263
    Input :
        3
        1 2 3
        1 3 2
    Output :
        2 1 3
*/

#include <iostream>

#define MAX_N 1000001

int inorder[MAX_N];
int postorder[MAX_N];

void dft(int inLow, int inHigh, int postLow, int postHigh)
{
    if ((inLow <= inHigh) && (postLow <= postHigh))
    {
        int root = postorder[postHigh];
        printf("%d ", root);

        int pivot = 0;
        for (pivot; inorder[pivot] != root; pivot++)
            ;
        int nLeft = pivot - inLow;
        int nRight = inHigh - pivot;
        dft(inLow, inLow + nLeft - 1, postLow, postLow + nLeft - 1);
        dft(inHigh - nRight + 1, inHigh, postHigh - nRight, postHigh - 1);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &inorder[i]);
    }
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &postorder[i]);
    }

    dft(0, n - 1, 0, n - 1);

    return 0;
}
