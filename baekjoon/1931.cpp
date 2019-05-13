/*
    1931 : 회의실배정
    URL : https://www.acmicpc.net/problem/1931
    Input :
        11
        1 4
        3 5
        0 6
        5 7
        3 8
        5 9
        6 10
        8 11
        8 12
        2 13
        12 14
    Output :
        4
*/

#include <iostream>
#include <algorithm>
#include <vector>

int main(int argc, char const *argv[])
{
    std::vector<std::pair<int, int>> meetings;

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::pair<int, int> meeting;
        std::cin >> meeting.second;
        std::cin >> meeting.first;

        meetings.push_back(meeting);
    }

    std::sort(meetings.begin(), meetings.end());

    int count = 1;
    int endtime = meetings[0].first;
    for (int i = 1; i < n; i++)
    {
        if (meetings[i].second < endtime)
        {
            continue;
        }
        endtime = meetings[i].first;
        count++;
    }

    std::cout << count;

    return 0;
}
