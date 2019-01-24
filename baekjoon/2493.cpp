/*
    2493 : 탑
    URL : https://www.acmicpc.net/problem/2493
    Input :
        5
        6 9 5 7 4
    Output :
        0 0 2 2 4
*/

#include <stdio.h>

#define MAX_N 500001

int N;

int index[MAX_N];
int stack[MAX_N];

int main(int argc, char const *argv[])
{
    scanf("%d", &N);

    int top = 0;
    int height = 0;

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &height);

        while (top > 0)
        {
            if (stack[top] > height)
            {
                printf("%d ", index[top]);
                break;
            }
            top--;
        }

        if (top == 0)
        {
            printf("0 ");
        }

        top++;
        index[top] = i + 1;
        stack[top] = height;
    }

    return 0;
}
