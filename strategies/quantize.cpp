/*
    QUANTIZE : Quantization
    Difficulty : 중
    Input :
        2
        10 3
        3 3 3 1 2  3 2 2 2 1
        9 3
        1 744 755 4 897 902 890 6 777
    Output :
        0
        651
*/
#include <iostream>
#include <cstring>
#include <algorithm>

#define MAX_N 1001
#define MAX_S 11

using namespace std;

const int POSINF = 987654321;

int N;
int S;

int A[MAX_N];
int SUM[MAX_N];
int SQ_SUM[MAX_N];

int cache[MAX_N][MAX_S];

void init()
{
    sort(A, A + N);

    SUM[0] = A[0];
    SQ_SUM[0] = A[0] * A[0];

    for (int i = 1; i <= N; i++)
    {
        SUM[i] = SUM[i - 1] + A[i];
        SQ_SUM[i] = SQ_SUM[i - 1] + (A[i] * A[i]);
    }
}

int minError(int low, int high)
{
    int sum = SUM[high] - (low == 0 ? 0 : SUM[low - 1]);
    int sqSum = SQ_SUM[high] - (low == 0 ? 0 : SQ_SUM[low - 1]);

    int m = int(0.5 + (double)sum / (high - low + 1));
    return sqSum - (2 * m * sum) + (m * m * (high - low + 1));
}

int quantize(int from, int parts)
{
    int &ret = cache[from][parts];

    if (from == N)
    {
        return 0;
    }

    if (parts == 0)
    {
        return POSINF;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = POSINF;
    for (int partSize = 1; (from + partSize) <= N; partSize++)
    {
        ret = min(ret,
                  quantize(from + partSize, parts - 1) + minError(from, from + partSize - 1));
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        memset(&(A[0]), 0, sizeof(int) * MAX_N);
        memset(&(SUM[0]), 0, sizeof(int) * MAX_N);
        memset(&(SQ_SUM[0]), 0, sizeof(int) * MAX_N);
        memset(&(cache[0][0]), -1, sizeof(int) * MAX_N * MAX_S);

        cin >> N;
        cin >> S;

        for (int j = 0; j < N; j++)
        {
            cin >> A[j];
        }

        init();

        cout << quantize(0, S) << endl;
    }

    return 0;
}
