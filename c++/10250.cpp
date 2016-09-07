#include <iostream>

int main()
{
    int T;
    std::cin >> T;
    while (T--)
    {
        int room = 0;
        int H, W, N;
        int h = 1;
        int w = 1;
        std::cin >> H >> W >> N;
        for (int i = 1; i < N; ++i)
        {
            h++;
            if (h > H)
            {
                h = 1;
                w++;
            }
        }
        room = (h * 100) + w;
        std::cout << room << std::endl;
    }
    return 0;
}