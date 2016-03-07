#include <iostream>

bool has(int*, int, int);

int main()
{
	int N, M;
	int *broken;
	std::cin >> N;
	std::cin >> M;

	broken = new int[M];
	for (int i = 0; i < M; ++i)
	{
		int n;
		std::cin >> n;
		broken[i] = n;
	}

	int channel = N;
	if (channel == 100)
	{
		std::cout << 0;
		return 0;
	}

	int near = 0;
	int key = 1000000;
	int button = 0;
	while ((channel / key) == 0)
	{
		key = key / 10;
	}
	while (key != 0 && (channel / key) > 0)
	{
		int number = channel / key;
		std::cout << "number=" << number << std::endl;
		while (has(broken, M, number))
		{
			number++;
		}
		near += number * key;
		channel = channel % key;
		key = key / 10;
		button++;
		std::cout << "near=" << near << "channel=" << channel << ", key=" << key << ", button=" << button << std::endl;
	}
	if (N > near)
	{
		button += (N - near);
	}
	else
	{
		button += (near - N);
	}
	std::cout << button;
	return 0;
}

bool has(int* arr, int len, int target)
{
	for (int i = 0; i < len; i++)
	{
		if (arr[i] == target)
		{
			return true;
		}
	}
	return false;
}