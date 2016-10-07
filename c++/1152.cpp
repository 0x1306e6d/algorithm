/*
    1152 : 단어의 개수
    URL : https://www.acmicpc.net/problem/1152
    Input :
        The Curious Case of Benjamin Button
    Output :
        6
*/
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1000000
using namespace std;

int main()
{
    char sentence[MAX];
    fgets(sentence, MAX, stdin);

    int i = 0;
    int count = 0;
    int length = strlen(sentence);

    if (sentence[0] == ' ')
    {
        i++;
    }
    if (sentence[length - 1] == '\n')
    {
        length--;
    }
    if (sentence[length - 1] == ' ')
    {
        length--;
    }
    if (length == 0)
    {
        cout << 0;
        return 0;
    }

    for (i; i < length; ++i)
    {
        if (sentence[i] == ' ')
        {
            count++;
        }
    }
    cout << (count + 1);
    return 0;
}