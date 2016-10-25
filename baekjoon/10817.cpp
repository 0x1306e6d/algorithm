#include <iostream>

int main()
{
	int max;
	int a, b, c;
	std::cin >> a >> b >> c;

	if (a > b)
	{
		if (b > c)
		{
			std::cout << b;
		}
		else
		{
			if (c > a)
			{
				std::cout << a;
			}
			else
			{
				std::cout << c;
			}
		}
	}
	else if (b > a)
	{
		if (a > c)
		{
			std::cout << a;
		}
		else
		{
			if (c > b)
			{
				std::cout << b;
			}
			else
			{
				std::cout << c;
			}
		}
	}
	else
	{
		std::cout << a;
	}
}