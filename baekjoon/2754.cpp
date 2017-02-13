/*
    2754 : 학점계산
    URL : https://www.acmicpc.net/problem/2754
    Input :
        A0
    Output :
        4.0
*/
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    char prefix;
    cin >> prefix;
    if (prefix == 'F')
    {
        printf("0.0");
    }
    else
    {
        double score = 0.0;

        char postfix;
        cin >> postfix;

        switch (prefix)
        {
        case 'A':
            score += 4.0;
            break;
        case 'B':
            score += 3.0;
            break;
        case 'C':
            score += 2.0;
            break;
        case 'D':
            score += 1.0;
            break;
        }
        switch (postfix)
        {
        case '+':
            score += 0.3;
            break;
        case '-':
            score -= 0.3;
            break;
        }

        printf("%.1f", score);
    }

    return 0;
}