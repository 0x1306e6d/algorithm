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

#define MAX 101

using namespace std;

typedef struct _point
{
    char x;
    char y;
} Point;

typedef struct _node
{
    short path_cost;
    Point point;
} Node;

int SearchAStar();
bool GoalTest(Point point);
Point MakePoint(int x, int y);
Node MakeNode(int path_cost, int x, int y);

int N, M;
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
    queue<Node> frontier;
    bool frontierCheck[MAX][MAX] = {0};
    bool explored[MAX][MAX] = {0};

    frontier.push(MakeNode(1, 0, 0));
    while (1)
    {
        if (frontier.empty())
        {
            // Failure
            return -1;
        }

        Node node = frontier.front();
        frontier.pop();
        frontierCheck[node.point.x][node.point.y] = 1;
        explored[node.point.x][node.point.y] = 1;

        // Top
        if ((node.point.y > 0) && (TABLE[node.point.x][node.point.y - 1] == 1))
        {
            Node child = MakeNode(node.path_cost + 1, node.point.x, (node.point.y - 1));
            if (frontierCheck[child.point.x][child.point.y] == 0 && explored[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.path_cost;
                }
                else
                {
                    frontier.push(child);
                }
            }
        }

        // Bottom
        if ((node.point.y < N) && (TABLE[node.point.x][node.point.y + 1] == 1))
        {
            Node child = MakeNode(node.path_cost + 1, node.point.x, (node.point.y + 1));
            if (frontierCheck[child.point.x][child.point.y] == 0 && explored[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.path_cost;
                }
                else
                {
                    frontier.push(child);
                }
            }
        }

        // Left
        if ((node.point.x > 0) && (TABLE[node.point.x - 1][node.point.y] == 1))
        {
            Node child = MakeNode(node.path_cost + 1, (node.point.x - 1), node.point.y);
            if (frontierCheck[child.point.x][child.point.y] == 0 && explored[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.path_cost;
                }
                else
                {
                    frontier.push(child);
                }
            }
        }

        // Right
        if ((node.point.x < M) && (TABLE[node.point.x + 1][node.point.y] == 1))
        {
            Node child = MakeNode(node.path_cost + 1, (node.point.x + 1), node.point.y);
            if (frontierCheck[child.point.x][child.point.y] == 0 && explored[child.point.x][child.point.y] == 0)
            {
                if (GoalTest(child.point))
                {
                    return child.path_cost;
                }
                else
                {
                    frontier.push(child);
                }
            }
        }

        frontierCheck[node.point.x][node.point.y] = 0;
    }

    // Failure
    return -1;
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

Node MakeNode(int path_cost, int x, int y)
{
    Node node;
    Point point = MakePoint(x, y);

    node.path_cost = (short)path_cost;
    node.point = point;

    return node;
}