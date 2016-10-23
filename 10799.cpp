/*
    10799 : 쇠막대기
    URL :
    Input #1 :
        ()(((()())(())()))(())
    Output #1 :
        17
    Input #2 :
        (((()(()()))(())()))(()())
    Output #2 :
        24
*/
#include <iostream>
#include <vector>
#include <string.h>

#define MAX 100000
#define RASER 0
#define BAT 1
using namespace std;

int TOTAL;
int LENGTH;
char LINE[MAX];

struct _node
{
    int index;
    int type;
    struct _node* parent;
    vector<struct _node*> childs;
};
typedef struct _node node;

void addNode(node* parent, node* node);
int countRaser(node* node);

int main()
{
    cin >> LINE;
    LENGTH = strlen(LINE);

    node root;
    root.index = -1;

    node* temp = &root;
    for (int i = 0; i < LENGTH; ++i)
    {
        if (LINE[i] == '(')
        {
            node* n = new node();
            n->index = i;
            n->parent = temp;

            addNode(temp, n);
            temp = n;
        }
        else if (LINE[i] == ')')
        {
            if (temp->index + 1 == i)
            {
                temp->type = RASER;
            }
            else
            {
                temp->type = BAT;
            }
            temp = temp->parent;
        }
    }

    for (vector<struct _node*>::iterator it = root.childs.begin(); it != root.childs.end(); ++it)
    {
        if ((*it)->type == BAT)
        {
            countRaser(*it);
        }
    }
    
    cout << TOTAL;
    return 0;
}

void addNode(node* parent, node* node)
{
    parent->childs.push_back(node);
}

int countRaser(node* node)
{
    int count = 0;

    for (vector<struct _node*>::iterator it = node->childs.begin(); it != node->childs.end(); ++it)
    {
        if ((*it)->type == BAT)
        {
            count += countRaser(*it);
        }
        else
        {
            count++;
        }
    }
    TOTAL += count + 1;

    return count;
}