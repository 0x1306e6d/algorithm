/*
    MEETINGROOM : 회의실 배정
    Difficulty : 상
    Input :
        3
        2
        1 10 10 20
        1 10 10 20
        3
        1 10 10 20
        1 10 10 20
        1 10 10 20
        3
        2 5 6 9
        1 3 8 10
        4 7 11 12
    Output :
        POSSIBLE
        10 20
        1 10
        IMPOSSIBLE
        POSSIBLE
        2 5
        8 10
        11 12
*/

#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>

std::vector<std::vector<int>> adjacents;

std::vector<int> sccId;
std::vector<int> sccDiscovered;
std::stack<int> sccStack;
int sccCounter;
int sccVertexCounter;

bool disjoint(const std::pair<int, int> &a, const std::pair<int, int> &b)
{
    return (a.second <= b.first) || (a.first >= b.second);
}

void mkgraph(const std::vector<std::pair<int, int>> &meetings)
{
    int nmeetings = meetings.size();

    adjacents.clear();
    adjacents.resize(nmeetings * 2);

    for (int i = 0; i < nmeetings; i += 2)
    {
        int j = i + 1;
        adjacents[i * 2 + 1].push_back(j * 2);
        adjacents[j * 2 + 1].push_back(i * 2);
    }

    for (int i = 0; i < nmeetings; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (!disjoint(meetings[i], meetings[j]))
            {
                adjacents[i * 2].push_back(j * 2 + 1);
                adjacents[j * 2].push_back(i * 2 + 1);
            }
        }
    }
}

int scc(int here)
{
    sccDiscovered[here] = sccVertexCounter++;
    int ret = sccDiscovered[here];

    sccStack.push(here);
    for (int i = 0; i < adjacents[here].size(); i++)
    {
        int there = adjacents[here][i];

        if (sccDiscovered[there] == -1)
        {
            ret = std::min(ret, scc(there));
        }
        else if (sccId[there] == -1)
        {
            ret = std::min(ret, sccDiscovered[there]);
        }
    }

    if (ret == sccDiscovered[here])
    {
        while (true)
        {
            int top = sccStack.top();
            sccStack.pop();

            sccId[top] = sccCounter;
            if (top == here)
            {
                break;
            }
        }
        sccCounter++;
    }

    return ret;
}

std::vector<int> tarjanSCC(void)
{
    int nadjacents = adjacents.size();

    sccId = std::vector<int>(nadjacents, -1);
    sccDiscovered = std::vector<int>(nadjacents, -1);

    sccCounter = 0;
    sccVertexCounter = 0;

    for (int i = 0; i < nadjacents; i++)
    {
        if (sccDiscovered[i] == -1)
        {
            scc(i);
        }
    }

    return sccId;
}

std::vector<int> solveTwoSAT(void)
{
    int nadjacents = adjacents.size() / 2;

    std::vector<int> label = tarjanSCC();

    for (int i = 0; i < (2 * nadjacents); i += 2)
    {
        if (label[i] == label[i + 1])
        {
            return std::vector<int>();
        }
    }

    std::vector<int> value(2 * nadjacents, -1);

    std::vector<std::pair<int, int>> order;
    for (int i = 0; i < (2 * nadjacents); i++)
    {
        order.push_back(std::make_pair(-label[i], i));
    }
    std::sort(order.begin(), order.end());

    for (int i = 0; i < (2 * nadjacents); i++)
    {
        int vertex = order[i].second;
        int index = vertex / 2;
        int isTrue = (vertex % 2) == 0;

        if (value[index] != -1)
        {
            continue;
        }

        value[index] = !isTrue;
    }

    return value;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        std::vector<std::pair<int, int>> meetings;

        int n;
        std::cin >> n;

        for (int i = 0; i < n; i++)
        {
            std::pair<int, int> ab;
            std::pair<int, int> cd;

            std::cin >> ab.first;
            std::cin >> ab.second;
            meetings.push_back(ab);

            std::cin >> cd.first;
            std::cin >> cd.second;
            meetings.push_back(cd);
        }

        mkgraph(meetings);

        std::vector<int> twoSAT = solveTwoSAT();
        if (twoSAT.empty())
        {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
        else
        {
            std::cout << "POSSIBLE" << std::endl;
            for (int i = 0; i < (2 * n); i += 2)
            {
                if (twoSAT[i] == 1)
                {
                    std::cout << meetings[i].first << " ";
                    std::cout << meetings[i].second << std::endl;
                }
                else
                {
                    std::cout << meetings[i + 1].first << " ";
                    std::cout << meetings[i + 1].second << std::endl;
                }
            }
        }
    }

    return 0;
}
