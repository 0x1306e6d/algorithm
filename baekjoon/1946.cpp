/*
    1946 : 신입 사원
    URL : https://www.acmicpc.net/problem/1946
    Input :
        2
        5
        3 2
        1 4
        4 1
        2 3
        5 5
        7
        3 6
        7 3
        4 2
        1 4
        5 7
        2 5
        6 1
    Output :
        4
        3
*/

#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_N 100001

struct applicant
{
    int document;
    int interview;
};

bool comp(const applicant &a, const applicant &b)
{
    return (a.document < b.document);
}

int main(int argc, char const *argv[])
{
    int t;
    std::cin >> t;

    while (t--)
    {
        int n;
        std::cin >> n;

        std::vector<struct applicant> applicants(n);

        for (int i = 0; i < n; i++)
        {
            std::cin >> applicants[i].document;
            std::cin >> applicants[i].interview;
        }

        std::sort(applicants.begin(), applicants.end(), comp);

        int failCount = 0;
        int maxInterview = MAX_N;
        for (int i = 0; i < n; i++)
        {
            const int document = applicants[i].document;
            const int interview = applicants[i].interview;

            bool fail = false;
            if (interview > maxInterview)
            {
                failCount += 1;
            }
            else
            {
                maxInterview = interview;
            }
        }

        std::cout << (n - failCount) << std::endl;
    }

    return 0;
}
