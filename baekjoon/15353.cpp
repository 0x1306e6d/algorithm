/*
    15353 : 큰 수 A+B (2)
    URL : https://www.acmicpc.net/problem/15353
    Input :
        9223372036854775807 9223372036854775808
    Output :
        18446744073709551615
*/

#include <iostream>
#include <string>

#define MAX_N 10001

int c[MAX_N];

int plus(std::string &a, std::string &b)
{
    if (a.length() > b.length())
    {
        return plus(b, a);
    }

    int aSize = a.size();
    int bSize = b.size();
    int ret = 0;
    for (; ret < a.length(); ret++)
    {
        c[ret] += (a[aSize - ret - 1] + b[bSize - ret - 1] - 96);
    }
    for (; ret < b.length(); ret++)
    {
        c[ret] += (b[bSize - ret - 1] - 48);
    }
    for (int i = 0; i < ret; i++)
    {
        if (c[i] >= 10)
        {
            c[i + 1] += (c[i] / 10);
            c[i] = (c[i] % 10);

            if (i == (ret - 1))
            {
                ret++;
            }
        }
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    std::string a;
    std::string b;
    std::cin >> a;
    std::cin >> b;

    int size = plus(a, b);
    for (int i = 0; i < size; i++)
    {
        std::cout << c[size - i - 1];
    }

    return 0;
}
