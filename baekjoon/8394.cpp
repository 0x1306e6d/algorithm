/*
    8394 : 악수
    URL : https://www.acmicpc.net/problem/8394
    Input :
		4
    Output :
		5
*/

#include <iostream>

int main(int argc, char const *argv[])
{
	int n;
	std::cin >> n;

	int a = 0;
	int b = 1;
	int answer = 0;

	for (int i = 0; i < n; i++)
	{
		answer = (a + b) % 10;

		a = b;
		b = answer;
	}

	std::cout << answer;

	return 0;
}
