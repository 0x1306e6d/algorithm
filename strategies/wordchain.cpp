/*
    WORDCHAIN : 단어 제한 끝말잇기
    Difficulty : 하
    Input :
        3
        4
        dog
        god
        dragon
        need
        3
        aa
        ab
        bb
        2
        ab
        cd
    Output :
        need dog god dragon
        aa ab bb
        IMPOSSIBLE
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#define MAX_ALPHABET 26

std::vector<std::vector<int>> adjacents;
std::vector<std::string> graph[MAX_ALPHABET][MAX_ALPHABET];
std::vector<int> indegree;
std::vector<int> outdegree;

void clear(void)
{
    for (int i = 0; i < MAX_ALPHABET; i++)
    {
        for (int j = 0; j < MAX_ALPHABET; j++)
        {
            graph[i][j].clear();
        }
    }
    adjacents = std::vector<std::vector<int>>(
        MAX_ALPHABET, std::vector<int>(MAX_ALPHABET, 0));
    indegree = std::vector<int>(MAX_ALPHABET, 0);
    outdegree = std::vector<int>(MAX_ALPHABET, 0);
}

void mkgraph(std::vector<std::string> &words)
{
    for (int i = 0; i < words.size(); i++)
    {
        std::string word = words[i];

        int start = word[0] - 'a';
        int end = word[word.size() - 1] - 'a';

        graph[start][end].push_back(word);
        adjacents[start][end]++;
        indegree[end]++;
        outdegree[start]++;
    }
}

bool hasEulerCircuitOrTrail(void)
{
    int in = 0;
    int out = 0;

    for (int i = 0; i < MAX_ALPHABET; i++)
    {
        int delta = (outdegree[i] - indegree[i]);

        if ((delta < -1) || (delta > 1))
        {
            return false;
        }
        if (delta == 1)
        {
            in++;
        }
        if (delta == -1)
        {
            out++;
        }
    }

    if (((in == 0) && (out == 0)) || ((in == 1) && (out == 1)))
    {
        return true;
    }
    else
    {
        return false;
    }
}

void getEulerCircuit(int here, std::vector<int> &eulerCircuit)
{
    for (int there = 0; there < adjacents.size(); there++)
    {
        while (adjacents[here][there] > 0)
        {
            adjacents[here][there]--;
            getEulerCircuit(there, eulerCircuit);
        }
    }
    eulerCircuit.push_back(here);
}

std::vector<int> getEulerCircuitOrTrail(void)
{
    std::vector<int> eulerCircuitOrTrail;

    for (int i = 0; i < MAX_ALPHABET; i++)
    {
        if ((indegree[i] + 1) == outdegree[i])
        {
            getEulerCircuit(i, eulerCircuitOrTrail);
            return eulerCircuitOrTrail;
        }
    }

    for (int i = 0; i < MAX_ALPHABET; i++)
    {
        if (outdegree[i] > 0)
        {
            getEulerCircuit(i, eulerCircuitOrTrail);
            return eulerCircuitOrTrail;
        }
    }

    return eulerCircuitOrTrail;
}

std::string wordchain(std::vector<std::string> &words)
{
    clear();
    mkgraph(words);

    if (!hasEulerCircuitOrTrail())
    {
        return "IMPOSSIBLE";
    }

    std::vector<int> eulerCircuitOrTrail = getEulerCircuitOrTrail();
    if (eulerCircuitOrTrail.size() != (words.size() + 1))
    {
        return "IMPOSSIBLE";
    }

    std::reverse(eulerCircuitOrTrail.begin(), eulerCircuitOrTrail.end());

    std::string result;
    for (int i = 1; i < eulerCircuitOrTrail.size(); i++)
    {
        int start = eulerCircuitOrTrail[i - 1];
        int end = eulerCircuitOrTrail[i];

        if (i > 1)
        {
            result.append(" ");
        }

        result.append(graph[start][end].back());
        graph[start][end].pop_back();
    }
    return result;
}

int main(int argc, char const *argv[])
{
    int C;
    std::cin >> C;

    for (int c = 0; c < C; c++)
    {
        int n;
        std::cin >> n;

        std::vector<std::string> words;

        for (int i = 0; i < n; i++)
        {
            std::string word;
            std::cin >> word;

            words.push_back(word);
        }

        std::cout << wordchain(words) << std::endl;
    }

    return 0;
}