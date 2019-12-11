/*
    10825: 국영수
    URL: https://www.acmicpc.net/problem/10825
    Input:
        12
        Junkyu 50 60 100
        Sangkeun 80 60 50
        Sunyoung 80 70 100
        Soong 50 60 90
        Haebin 50 60 100
        Kangsoo 60 80 100
        Donghyuk 80 60 100
        Sei 70 70 70
        Wonseob 70 70 90
        Sanghyun 70 70 80
        nsj 80 80 80
        Taewhan 50 60 90
    Output:
        Donghyuk
        Sangkeun
        Sunyoung
        nsj
        Wonseob
        Sanghyun
        Sei
        Kangsoo
        Haebin
        Junkyu
        Soong
        Taewhan
*/

#include <iostream>
#include <vector>

struct student
{
    std::string name;
    int korean;
    int english;
    int math;
};

std::vector<struct student> temp;
std::vector<struct student> students;

void merge(int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;

    while ((i <= mid) && (j <= right))
    {
        if (students[i].korean > students[j].korean)
        {
            temp[k] = students[i];
            i++;
        }
        else if (students[i].korean < students[j].korean)
        {
            temp[k] = students[j];
            j++;
        }
        else
        {
            if (students[i].english < students[j].english)
            {
                temp[k] = students[i];
                i++;
            }
            else if (students[i].english > students[j].english)
            {
                temp[k] = students[j];
                j++;
            }
            else
            {
                if (students[i].math > students[j].math)
                {
                    temp[k] = students[i];
                    i++;
                }
                else if (students[i].math < students[j].math)
                {
                    temp[k] = students[j];
                    j++;
                }
                else
                {
                    if (students[i].name < students[j].name)
                    {
                        temp[k] = students[i];
                        i++;
                    }
                    else
                    {
                        temp[k] = students[j];
                        j++;
                    }
                }
            }
        }
        k++;
    }

    if (i > mid)
    {
        for (int l = j; l <= right; l++)
        {
            temp[k] = students[l];
            k++;
        }
    }
    else
    {
        for (int l = i; l <= mid; l++)
        {
            temp[k] = students[l];
            k++;
        }
    }

    for (int l = left; l <= right; l++)
    {
        students[l] = temp[l];
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

    temp = std::vector<struct student>(n);
    students = std::vector<struct student>(n);

    for (int i = 0; i < n; i++)
    {
        std::cin >> students[i].name;
        std::cin >> students[i].korean;
        std::cin >> students[i].english;
        std::cin >> students[i].math;
    }

    msort(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        std::cout << students[i].name << "\n";
    }

    return 0;
}
