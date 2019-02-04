/*
    DICTIONARY : 고대어 사전
    Difficulty : 하
    Input :
        3
        3
        ba
        aa
        ab
        5
        gg
        kia
        lotte
        lg
        hanhwa
        6
        dictionary
        english
        is
        ordered
        ordinary
        this
    Output :
        INVALID HYPOTHESIS
        ogklhabcdefijmnpqrstuvwxyz
        abcdefghijklmnopqrstuvwxyz
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vector_int;

vector<vector_int> adjacent;
vector_int seen;
vector_int order;

void mkgraph(const vector<string> &words)
{
    adjacent = vector<vector_int>(26, vector_int(26, 0));

    for (int j = 1; j < words.size(); j++)
    {
        int i = j - 1;
        int len = min(words[i].size(), words[j].size());

        for (int k = 0; k < len; k++)
        {
            if (words[i][k] != words[j][k])
            {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';
                adjacent[a][b] = 1;
                break;
            }
        }
    }
}

void dfs(int here)
{
    seen[here] = 1;
    for (int there = 0; there < adjacent.size(); there++)
    {
        if ((adjacent[here][there] == 1) && !seen[there])
        {
            dfs(there);
        }
    }
    order.push_back(here);
}

vector_int tsort(void)
{
    int n = adjacent.size();
    seen = vector_int(n, 0);
    order = vector_int();

    for (int i = 0; i < n; i++)
    {
        if (!seen[i])
        {
            dfs(i);
        }
    }
    reverse(order.begin(), order.end());

    for (int i = 0; i < n; i++)
    {
        for (int j = (i + 1); j < n; j++)
        {
            if (adjacent[order[j]][order[i]])
            {
                return vector_int();
            }
        }
    }
    return order;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int n;
        vector<string> words;

        cin >> n;

        for (int j = 0; j < n; j++)
        {
            string word;

            cin >> word;

            words.push_back(word);
        }

        mkgraph(words);
        vector_int t = tsort();

        if (t.size() == 0)
        {
            printf("INVALID HYPOTHESIS\n");
        }
        else
        {
            for (int i = 0; i < t.size(); i++)
            {
                printf("%c", t[i] + 'a');
            }
            printf("\n");
        }
    }

    return 0;
}
