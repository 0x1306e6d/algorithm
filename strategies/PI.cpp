/*
    PI : 원주율 외우기
    Difficulty : 하
    Input :
        5 
        12341234 
        11111222 
        12122222 
        22222222 
        12673939 
    Output :
        4
        2
        5
        2
        14
*/
#include <iostream>
#include <cstring>

#define MAX_N 100001

using namespace std;

const int POSINF = 987654321;
int cache[MAX_N];

int classify(string &N, int start, int end)
{
    bool flag1 = true;
    bool flag2 = true;
    string M = N.substr(start, end - start + 1);

    // 모든 숫자가 같을 때
    for (int i = 0; i < M.size(); i++)
    {
        if (M[i] != M[0])
        {
            flag1 = false;
            break;
        }
    }
    if (flag1)
    {
        return 1;
    }

    // 숫자가 1씩 단조 증가하거나 단조 감소할 때
    flag1 = true;
    for (int i = 0; i < (M.size() - 1); i++)
    {
        if ((M[i + 1] - M[i]) != (M[1] - M[0]))
        {
            flag1 = false;
            break;
        }
    }
    if (flag1 && (abs(M[1] - M[0]) == 1))
    {
        return 2;
    }

    // 두 개의 숫자가 번갈아가며 나타날 때
    for (int i = 0; i < M.size(); i++)
    {
        if (M[i] != M[i % 2])
        {
            flag2 = false;
            break;
        }
    }
    if (flag2)
    {
        return 4;
    }

    // 숫자가 등차 수열을 이룰 때
    if (flag1)
    {
        return 5;
    }

    // 이 외의 모든 경우
    return 10;
}

int memorize(string &N, int begin)
{
    int &ret = cache[begin];

    if (begin == N.size())
    {
        return 0;
    }

    if (ret != -1)
    {
        return ret;
    }

    ret = POSINF;
    for (int L = 3; L <= 5; L++)
    {
        if ((begin + L) <= N.size())
        {
            ret = min(ret,
                      memorize(N, begin + L) + classify(N, begin, begin + L - 1));
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
        string n;

        memset(&(cache[0]), -1, sizeof(int) * MAX_N);

        cin >> n;
        cout << memorize(n, 0) << endl;
    }

    return 0;
}
