/*
    WILDCARD : 와일드카드
    Difficulty : 중
    Input :
        2
        he?p
        3
        help
        heap
        helpp
        *p*
        3
        help
        papa
        hello
    Output :
        heap
        help
        help
        papa
*/
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

#define MAX_FILENAME 101

using namespace std;

int cache[MAX_FILENAME][MAX_FILENAME];

int match1(const string &w, const string &filename)
{
    int pos = 0;

    while (pos < w.size() &&
           pos < filename.size() &&
           (w[pos] == '?' || w[pos] == filename[pos]))
    {
        pos++;
    }

    if (pos == w.size())
    {
        return (pos == filename.size());
    }

    if (w[pos] == '*')
    {
        for (int skip = 0; (pos + skip) <= filename.size(); skip++)
        {
            if (match1(w.substr(pos + 1), filename.substr(pos + skip)))
            {
                return 1;
            }
        }
    }

    return 0;
}

int match2(string &W, string &filename, int w, int f)
{
    int &ret = cache[w][f];

    if (ret != -1)
    {
        return ret;
    }

    while (w < W.size() &&
           f < filename.size() &&
           (W[w] == '?' || W[w] == filename[f]))
    {
        w++;
        f++;
    }

    if (w == W.size())
    {
        ret = (f == filename.size());
        return ret;
    }

    if (W[w] == '*')
    {
        for (int skip = 0; (f + skip) <= filename.size(); skip++)
        {
            if (match2(W, filename, w + 1, f + skip))
            {
                ret = 1;
                return ret;
            }
        }
    }

    ret = 0;
    return ret;
}

int match3(string &W, string &filename, int w, int f)
{
    int &ret = cache[w][f];

    if (ret != -1)
    {
        return ret;
    }

    if (w < W.size() &&
        f < filename.size() &&
        (W[w] == '?' || W[w] == filename[f]))
    {
        ret = match3(W, filename, w + 1, f + 1);
        return ret;
    }

    if (w == W.size())
    {
        ret = (f == filename.size());
        return ret;
    }

    if (W[w] == '*')
    {
        if (match3(W, filename, w + 1, f) ||
            (f < filename.size() && match3(W, filename, w, f + 1)))
        {
            ret = 1;
            return ret;
        }
    }

    ret = 0;
    return ret;
}

int main(int argc, char const *argv[])
{
    int C;

    cin >> C;

    for (int i = 0; i < C; i++)
    {
        int N;
        string W;
        vector<string> V;
        vector<string>::iterator it;

        cin >> W;
        cin >> N;

        for (int j = 0; j < N; j++)
        {
            string filename;

            memset(&(cache[0][0]), -1, sizeof(int) * MAX_FILENAME * MAX_FILENAME);

            cin >> filename;

            if (match2(W, filename, 0, 0))
            {
                V.push_back(filename);
            }
        }

        sort(V.begin(), V.end());

        for (it = V.begin(); it != V.end(); ++it)
        {
            cout << (*it) << endl;
        }
    }

    return 0;
}
