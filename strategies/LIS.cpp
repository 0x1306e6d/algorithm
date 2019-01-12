/*
    LIS : Longest Increasing Sequence
    Difficulty : 하
    Input :
        3
        4
        1 2 3 4
        8
        5 4 3 2 1 6 7 8 
        8
        5 6 7 8 1 2 3 4
    Output :
        4
        4
        4
*/
#include <iostream>
#include <vector>
#include <cstring>

#define MAX_N 101

using namespace std;

int S[MAX_N];
int cache[MAX_N];

// int lis1(const vector<int> &S)
// {
//     int ret = 0;

//     if (S.empty())
//     {
//         return ret;
//     }

//     for (int i = 0; i < S.size(); i++)
//     {
//         vector<int> SS;

//         for (int j = i + 1; j < S.size(); j++)
//         {
//             if (S[i] < S[j])
//             {
//                 SS.push_back(S[j]);
//             }
//         }

//         ret = max(ret, 1 + lis1(SS));
//     }

//     return ret;
// }

int lis2(int n, int current)
{
    int &ret = cache[current];

    if (ret != -1)
    {
        return ret;
    }

    ret = 1;

    for (int next = current + 1; next < n; next++)
    {
        if (S[current] < S[next])
        {
            ret = max(ret, lis2(n, next) + 1);
        }
    }

    return ret;
}

int lis3(int n, int current)
{
    int &ret = cache[current + 1];

    if (ret != -1)
    {
        return ret;
    }

    ret = 1;

    for (int next = current + 1; next < n; next++)
    {
        if (current == -1 || S[current] < S[next])
        {
            ret = max(ret, lis3(n, next) + 1);
        }
    }

    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int N;

        memset(&(S[0]), 0, sizeof(int) * MAX_N);
        memset(&(cache[0]), -1, sizeof(int) * MAX_N);

        cin >> N;

        for (int j = 0; j < N; j++)
        {
            int n;

            cin >> n;

            S[j] = n;
        }

        cout << (lis3(N, -1) - 1) << endl;
    }

    return 0;
}
