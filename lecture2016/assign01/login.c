#include<stdio.h>
#include<stdlib.h>

int main() {
    int i, j, k;

    int SUM;
    int R, C;
    int K;
    int TIME_START, TIME_END;
    int DAY_START, DAY_END;
    int **TABLE;
    FILE *in, *out;
    in = fopen("login.inp", "r");
    out = fopen("login.out", "w");
    fscanf(in, "%d %d", &R, &C);
    // scanf("%d %d", &R, &C);

    TABLE = (int **) malloc(sizeof(int*) * R);
    for (i = 0; i < R; ++i) 
    {
        TABLE[i] = (int*) malloc(sizeof(int) * C);
        for (j = 0; j < C; ++j)
        {
            int count;
            fscanf(in, "%d", &count);
            // scanf("%d", &count);
            TABLE[i][j] = count;
        }
    }

    fscanf(in, "%d", &K);
    // scanf("%d", &K);
    for (i = 0; i < K; ++i)
    {
        fscanf(in, "%d %d %d %d",
        &DAY_START, &DAY_END,
        &TIME_START, &TIME_END);
        // scanf("%d %d %d %d",
        // &DAY_START, &DAY_END,
        // &TIME_START, &TIME_END);
        SUM = 0;

        for (j = (TIME_START - 1); j <= (TIME_END - 1); ++j)
        {
            for (k = (DAY_START - 1); k <= (DAY_END - 1); ++k)
            {
                SUM += TABLE[j][k];
            }
        }
        fprintf(out, "%d\n", SUM);
    }
    return 0;
}