#include <iostream>

int main()
{
	int a, b;
	int x, y;
	std::cin >> a >> b;
	std::cin >> x >> y;
	int start;
	if (y == 0)
	{
		start = a;
	}
	else
	{
		for (int i = 1; i <= x; i++)
		{
			if ((a + i) % x == y)
			{
				start = a + i;
				break;
			}
		}
	}
	for (start; start <= b; start += x)
	{

	}
	std::cout << start;
	return 0;
}