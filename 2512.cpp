#include <iostream>

using namespace std;

int main()
{
	int N, M;
	int sum = 0, big = 0;
	int* arr;
	cin >> N;
	arr = new int[N];
	for (int i = 0; i < N; ++i)
	{
		int n;
		cin >> n;
		arr[i] = n;
		sum += n;
		if (n > big)
		{
			big = n;
		}
	}
	cin >> M;

	if (sum <= M)
	{
		cout << big;
		return 0;
	}

	
/*
4
120 110 140 150
485
*/

	bool flag = false;
	int average = M / N;
	int remain = M;
	int count = 0;
	for (int i = 0; i < N; ++i)
	{
		if (arr[i] <= average)
		{
			remain -= arr[i];
		}
		else
		{
			count++;
			remain -= average;
		}
	}


	cout << "average=" << average << ", remain=" << remain << ", count=" << count << endl;
	cout << (average + (remain / count)) << endl;
	cout << sum;

	return 0;
}