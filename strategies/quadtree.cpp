/*
    QUADTREE : 쿼드 트리 뒤집기
    Difficulty : 하
    Input :
        4
        w
        xbwwb
        xbwxwbbwb
        xxwwwbxwxwbbbwwxxxwwbbbwwwwbb
    Output :
        w
        xwbbw
        xxbwwbbbw
        xxwbxwwxbbwwbwbxwbwwxwwwxbbwb
*/

#include <iostream>
#include <string>

std::string reverse(std::string::iterator &it)
{
    char head = *it;
    it++;

    if (head == 'w' || head == 'b')
    {
        return std::string(1, head);
    }
    else
    {
        std::string topLeft = reverse(it);
        std::string topRight = reverse(it);
        std::string bottomLeft = reverse(it);
        std::string bottomRight = reverse(it);
        return std::string("x") + bottomLeft + bottomRight + topLeft + topRight;
    }
}

int main(int argc, char const *argv[])
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        std::string compressed;
        std::cin >> compressed;

        std::string::iterator it = compressed.begin();
        std::cout << reverse(it) << std::endl;
    }

    return 0;
}
