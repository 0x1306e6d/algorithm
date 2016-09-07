#include <iostream>

int find_biggest(int a, int b);
bool is_bigger(int a, int b, int c);
void fraction_subtract(int* a, int* b, int c);

int main()
{
    int T;
    std::cin >> T;
    while (T--)
    {
        int a, b, c;
        std::cin >> a >> b;
        while (a > 1)
        {
            c = find_biggest(a, b);
            fraction_subtract(&a, &b, c);
        }
        std::cout << b << std::endl;
    }
    return 0;
}

int find_biggest(int a, int b)
{
    if (a == 1)
    {
        return b;
    }
    for (int i = 2; i <= b; ++i)
    {
        if (is_bigger(a, b, i))
        {
            return i;
        }
    }
    return b;
}

bool is_bigger(int a, int b, int c)
{
    return (a * c) >= b;
}

void fraction_subtract(int* a, int* b, int c)
{
    *a = (*a * c) - *b; 
    *b = *b * c;
}