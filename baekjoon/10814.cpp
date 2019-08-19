/*
    10814 : 나이순 정렬
    URL : https://www.acmicpc.net/problem/10814
    Input :
        3
        21 Junkyu
        21 Dohyun
        20 Sunyoung
    Output :
        20 Sunyoung
        21 Junkyu
        21 Dohyun
*/

#include <iostream>
#include <string>
#include <vector>

struct member
{
    int age;
    std::string name;
};

std::vector<struct member> temp;
std::vector<struct member> members;

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while ((i <= mid) && (j <= right))
    {
        if (members[i].age <= members[j].age)
        {
            temp[k] = members[i];
            i++;
        }
        else
        {
            temp[k] = members[j];
            j++;
        }
        k++;
    }

    if (i > mid)
    {
        for (int l = j; l <= right; l++)
        {
            temp[k] = members[l];
            k++;
        }
    }
    else
    {
        for (int l = i; l <= mid; l++)
        {
            temp[k] = members[l];
            k++;
        }
    }

    for (int l = left; l <= right; l++)
    {
        members[l] = temp[l];
    }
}

void msort(int left, int right)
{
    if (left < right)
    {
        int mid = (left + right) / 2;
        msort(left, mid);
        msort(mid + 1, right);

        merge(left, mid, right);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    temp = std::vector<struct member>(n);
    members = std::vector<struct member>(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> members[i].age;
        std::cin >> members[i].name;
    }

    msort(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        std::cout << members[i].age << " " << members[i].name << "\n";
    }

    return 0;
}
