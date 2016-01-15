#include<iostream>

int main()
{
	int n, x, d;
	std::cin >> n >> x;
	for (int i = 0; i < n; ++i)
	{
		std::cin >> d;
		if (d < x)
		{
			std::cout << d << " ";
		}
	}
	return 0;
}