/*
    10815 : 숫자 카드
    URL : https://www.acmicpc.net/problem/10815
    Input :
        5
        6 3 2 10 -10
        8
        10 9 -5 2 3 4 5 -10
    Output :
        1 0 0 1 1 0 0 1
*/

#include <iostream>
#include <algorithm>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> cards(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> cards[i];
    }
    std::sort(cards.begin(), cards.end());

    int m;
    std::cin >> m;

    std::vector<std::pair<int, int>> targets(m);
    for (int i = 0; i < m; i++)
    {
        int number;
        std::cin >> number;

        targets[i] = std::make_pair(number, i);
    }
    std::sort(targets.begin(), targets.end());

    std::vector<bool> answers(m, false);
    int i = 0;
    int j = 0;
    while ((i < cards.size()) && (j < targets.size()))
    {
        int card = cards[i];
        int target = targets[j].first;

        if (card == target)
        {
            answers[targets[j].second] = true;
            i++;
            j++;
        }
        else if (card > target)
        {
            j++;
        }
        else
        {
            i++;
        }
    }

    for (int i = 0; i < m; i++)
    {
        if (answers[i] == true)
        {
            std::cout << 1;
        }
        else
        {
            std::cout << 0;
        }
        if (i < (m - 1))
        {
            std::cout << " ";
        }
    }

    return 0;
}
