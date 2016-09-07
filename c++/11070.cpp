#include <iostream>
#include <cmath>

int main()
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int n, m;
        std::cin >> n;
        std::cin >> m;
        int scores[n];
        int losts[n];
        for (int j = 0; j < n; ++j)
        {
            scores[j] = 0;
            losts[j] = 0;
        }
        for (int j = 0; j < m; ++j)
        {
            int a, b, p, q;
            std::cin >> a;
            std::cin >> b;
            std::cin >> p;
            std::cin >> q;
            scores[a - 1] += p;
            losts[a - 1] += q;
            scores[b - 1] += q;
            losts[b - 1] += p;
        }
        int max = -987654321;
        int min = 987654321;
        for (int j = 0; j < n; ++j)
        {
            int W;
            int S = scores[j];
            int A = losts[j];
            if (S == 0)
            {
                W = 0;
            }
            else if (A == 0)
            {
                W = 1000;
            }
            else
            { 
                W = std::floor(1000LL * ((S * S) / (long double) ((S * S) + (A * A))));
            }

            if (W > max)
            {
                max = W;
            }
            if (W < min)
            {
                min = W;
            }
        }
        std::cout << max << std::endl;
        std::cout << min << std::endl;
    }
    return 0;
}