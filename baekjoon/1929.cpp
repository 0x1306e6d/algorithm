/*
    1929 : 소수 구하기
    URL : https://www.acmicpc.net/problem/1929
    Input :
        3 16
    Output :
        3
        5
        7
        11
        13
*/
#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }
    if (n == 2)
    {
        return true;
    }
    if ((n % 2) == 0)
    {
        return false;
    }

    int sqrtn = int(sqrt(n));
    for (int i = 3; i <= sqrtn; i += 2)
    {
        if ((n % i) == 0)
        {
            return false;
        }
    }

    return true;
}

int main(int argc, char const *argv[])
{
    int M;
    int N;

    ios::sync_with_stdio(false);

    cin >> M;
    cin >> N;

    for (int i = M; i <= N; i++)
    {
        if (is_prime(i))
        {
            cout << i << '\n';
        }
    }

    return 0;
}
