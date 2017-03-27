/*
    2178 : 미로 탐색
    URL : https://www.acmicpc.net/problem/2178
    Input #1:
        4 6
        101111
        101010
        101011
        111011
    Output #1:
        15
    Input #2:
        4 6
        110110
        110110
        111111
        111101
    Output #2:
        9
*/
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <stdio.h>

#define MAX 101

using namespace std;

typedef struct
{
    char x;
    char y;
} Point;

typedef struct
{
    int gn;
    int hn;
    Point point;
} Node;

int SearchAStar();
bool GoalTest(Point point);
Point MakePoint(int x, int y);
Node MakeNode(int gn, int x, int y);
int ParseHN(int x, int y);

int N;
int M;
bool TABLE[MAX][MAX];

int main()
{
    cin >> N;
    cin >> M;

    for (int y = 0; y < N; y++)
    {
        char column[M];
        cin >> column;

        for (int x = 0; x < M; x++)
        {
            if (column[x] == '1')
            {
                TABLE[x][y] = 1;
            }
            else
            {
                TABLE[x][y] = 0;
            }
        }
    }

    int min = SearchAStar();
    cout << min;

    return 0;
}

int SearchAStar()
{
    priority_queue<Node> frontier;
    bool frontierCheck[MAX][MAX] = {0};

    frontier.push(MakeNode(1, 0, 0));
    frontierCheck[0][0] = 1;
    while (1)
    {
        if (frontier.empty())
        {
            // Failure
            return -1;
        }

        Node node = frontier.top();
        frontier.pop();
        frontierCheck[node.point.x][node.point.y] = 0;

        // Top
        if ((node.point.y > 0) && (TABLE[node.point.x][node.point.y - 1] == 1))
        {
            Node child = MakeNode(node.gn + 1, node.point.x, (node.point.y - 1));
            if (frontierCheck[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.gn;
                }
                else
                {
                    frontier.push(child);
                    frontierCheck[child.point.x][child.point.y] = 1;
                }
            }
        }

        // Bottom
        if ((node.point.y < N) && (TABLE[node.point.x][node.point.y + 1] == 1))
        {
            Node child = MakeNode(node.gn + 1, node.point.x, (node.point.y + 1));
            if (frontierCheck[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.gn;
                }
                else
                {
                    frontier.push(child);
                    frontierCheck[child.point.x][child.point.y] = 1;
                }
            }
        }

        // Left
        if ((node.point.x > 0) && (TABLE[node.point.x - 1][node.point.y] == 1))
        {
            Node child = MakeNode(node.gn + 1, (node.point.x - 1), node.point.y);
            if (frontierCheck[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.gn;
                }
                else
                {
                    frontier.push(child);
                    frontierCheck[child.point.x][child.point.y] = 1;
                }
            }
        }

        // Right
        if ((node.point.x < M) && (TABLE[node.point.x + 1][node.point.y] == 1))
        {
            Node child = MakeNode(node.gn + 1, (node.point.x + 1), node.point.y);
            if (frontierCheck[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.gn;
                }
                else
                {
                    frontier.push(child);
                    frontierCheck[child.point.x][child.point.y] = 1;
                }
            }
        }
    }
}

bool GoalTest(Point point)
{
    return (point.x == (M - 1)) && (point.y == (N - 1));
}

Point MakePoint(int x, int y)
{
    Point point;

    point.x = (char)x;
    point.y = (char)y;

    return point;
}

Node MakeNode(int gn, int x, int y)
{
    Node node;
    int hn = ParseHN(x, y);
    Point point = MakePoint(x, y);

    node.gn = gn;
    node.hn = hn;
    node.point = point;

    return node;
}

int ParseHN(int x, int y)
{
    return (N - (y + 1)) + (M - (x + 1));
}

bool operator<(Node n1, Node n2)
{
    return (n1.gn + n1.hn) > (n2.gn + n2.hn);
}