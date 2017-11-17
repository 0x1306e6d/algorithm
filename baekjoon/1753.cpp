/*
    1753 : 최단경로
    URL : https://www.acmicpc.net/problem/1753
    Input :
      5 6
      1
      5 1 1
      1 2 2
      1 3 3
      2 3 4
      2 4 5
      3 4 6
    Output :
      0
      2
      3
      7
      INF
 */
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

#define INF 987654321
typedef pair<int, int> i_p_pair_t;
typedef pair<int, i_p_pair_t> d_i_p_pair_t;

struct edge_t {
        int u;
        int v;
        int w;
};

struct vertex_t {
        int id;
        vector<struct edge_t*> edges;
};

void find_shortest_path(struct vertex_t **vertices, int V, int start);

int main(int argc, char const *argv[]) {
        int V, E;
        int start;
        cin >> V >> E;
        cin >> start;

        struct vertex_t *vertices[V + 1];
        for (int i = 1; i <= V; i++)
        {
                vertices[i] = new struct vertex_t;
                vertices[i]->id = i;
        }

        for (int i = 0; i < E; i++)
        {
                int u, v, w;
                cin >> u >> v >> w;

                struct edge_t *p_edge = new struct edge_t;
                p_edge->u = u;
                p_edge->v = v;
                p_edge->w = w;

                struct vertex_t *p_vertex = vertices[u];
                p_vertex->edges.push_back(p_edge);
        }

        find_shortest_path(vertices, V, start);

        return 0;
}

void find_shortest_path(struct vertex_t **vertices, int V, int start)
{
        priority_queue<d_i_p_pair_t,
                       vector<d_i_p_pair_t>,
                       greater<d_i_p_pair_t> > q;

        int dist[V + 1];
        for (int i = 1; i <= V; i++)
                dist[i] = INF;
        dist[start] = 0;

        for (int i = 1; i <= V; i++)
        {
                struct vertex_t *p_vertex = vertices[i];
                if (p_vertex->id == start)
                {
                        i_p_pair_t i_p_pair = make_pair(p_vertex->id, p_vertex->id);
                        q.push(make_pair(0, i_p_pair));
                }
                else
                {
                        i_p_pair_t i_p_pair = make_pair(p_vertex->id, -1);
                        q.push(make_pair(INF, i_p_pair));
                }
        }

        while (!q.empty())
        {
                d_i_p_pair_t d_i_p_pair = q.top();
                i_p_pair_t i_p_pair = d_i_p_pair.second;
                q.pop();

                if (d_i_p_pair.first <= dist[i_p_pair.first])
                {
                        struct vertex_t *p_vertex = vertices[i_p_pair.first];

                        vector<struct edge_t*> edges = p_vertex->edges;
                        vector<struct edge_t*>::iterator it;
                        for (it = edges.begin(); it != edges.end(); ++it)
                        {
                                struct edge_t *p_edge = *it;

                                int old_distance = dist[p_edge->v];
                                int new_distance = dist[p_edge->u] + p_edge->w;
                                new_distance = min(old_distance, new_distance);
                                if (new_distance < old_distance)
                                {
                                        i_p_pair_t new_i_p_pair = make_pair(p_edge->v, p_edge->u);
                                        d_i_p_pair_t new_d_i_p_pair = make_pair(new_distance, new_i_p_pair);

                                        q.push(new_d_i_p_pair);
                                        dist[p_edge->v] = new_distance;
                                }
                        }
                }
        }

        for (int i = 1; i <= V; i++)
        {
                if (dist[i] == INF)
                        cout << "INF" << endl;
                else
                        cout << dist[i] << endl;
        }
}
