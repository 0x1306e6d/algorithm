/*
    FANMEETING : 팬미팅
    Difficulty : 상
    Input :
        4
        FFFMMM
        MMMFFF
        FFFFF
        FFFFFFFFFF
        FFFFM
        FFFFFMMMMF
        MFMFMFFFMMMFMF
        MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF
    Output :
        1
        6
        2
        2
*/

#include <iostream>
#include <string>
#include <vector>

typedef std::vector<int> ivector;

void add(ivector &a, ivector &b, int k)
{
    a.resize(std::max(a.size(), b.size() + k));
    for (int i = 0; i < b.size(); i++)
    {
        a[i + k] += b[i];
    }
}

void subtract(ivector &a, ivector &b)
{
    for (int i = 0; i < b.size(); i++)
    {
        a[i] -= b[i];
    }
}

ivector multiply(ivector &a, ivector &b)
{
    ivector c(a.size() + b.size() + 1, 0);
    for (int i = 0; i < a.size(); i++)
    {
        for (int j = 0; j < b.size(); j++)
        {
            c[i + j] += (a[i] * b[j]);
        }
    }
    return c;
}

ivector karatsuba(ivector &a, ivector &b)
{
    if (a.size() < b.size())
    {
        return karatsuba(b, a);
    }

    if ((a.size() == 0) || (b.size() == 0))
    {
        return ivector();
    }

    if (a.size() <= 64)
    {
        return multiply(a, b);
    }

    int mid = (a.size() / 2);
    ivector a0(a.begin(), a.begin() + mid);
    ivector a1(a.begin() + mid, a.end());
    ivector b0(b.begin(), b.begin() + std::min<int>(mid, b.size()));
    ivector b1(b.begin() + std::min<int>(mid, b.size()), b.end());

    // z2 = a1 * b1
    ivector z2 = karatsuba(a1, b1);
    // z0 = a0 * b0
    ivector z0 = karatsuba(a0, b0);
    // a0 = a0 + a1
    add(a0, a1, 0);
    // b0 = b0 + b1
    add(b0, b1, 0);
    // z1 = (a0 * b0) - z2 - z0
    ivector z1 = karatsuba(a0, b0);
    subtract(z1, z2);
    subtract(z1, z0);

    // c = z2 * (10 ^ (mid * 2)) + z1 * (10 ^ mid) + z0
    ivector c;
    add(c, z2, mid * 2);
    add(c, z1, mid);
    add(c, z0, 0);
    return c;
}

int hug(std::string &members, std::string &fans)
{
    ivector a(members.size());
    ivector b(fans.size());

    for (int i = 0; i < members.size(); i++)
    {
        a[i] = (members[i] == 'M');
    }
    for (int i = 0; i < fans.size(); i++)
    {
        b[fans.size() - i - 1] = (fans[i] == 'M');
    }

    ivector c = multiply(a, b);
    int count = 0;
    for (int i = (members.size() - 1); i < fans.size(); i++)
    {
        if (c[i] == 0)
        {
            count++;
        }
    }
    return count;
}

int main(int argc, char const *argv[])
{
    std::ios::sync_with_stdio(false);

    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        std::string members;
        std::string fans;

        std::cin >> members;
        std::cin >> fans;

        std::cout << hug(members, fans) << std::endl;
    }

    return 0;
}
