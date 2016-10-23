#include<iostream>

using namespace std;

int main()
{
	int n, c;
	unsigned long long first = 1;
	unsigned long long second = 2;
	unsigned long long next;
	cin >> n;
	if (n == 1)
	{
		cout << 1;
		return 0;
	}
	if (n == 2)
	{
		cout << 2;
		return 0;
	}
	for (c = 0; c < n; c++)
	{
		if (c <= 1)
			next = c;
		else
		{
			next = first + second;
			first = second;
			second = next;
		}
	}
	cout << (next % 10);

	return 0;
}