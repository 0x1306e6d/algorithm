/*
    2512: 예산
    URL: https://www.acmicpc.net/problem/2512
    Input:
		4
		120 110 140 150
		485
    Output:
		127
*/

#include <iostream>
#include <algorithm>
#include <vector>

int main(int argc, char const *argv[])
{
	std::vector<int> budgets;

	int n;
	std::cin >> n;

	int sumBudget = 0;
	for (int i = 0; i < n; i++)
	{
		int budget;
		std::cin >> budget;

		sumBudget += budget;

		budgets.push_back(budget);
	}

	std::sort(budgets.begin(), budgets.end());

	int m;
	std::cin >> m;

	if (sumBudget <= m)
	{
		std::cout << budgets.back();
	}
	else
	{
		int sum = 0;
		int maxBudget = 0;
		int maxBudgetLimit = 0;

		for (int i = 0; i < n; i++)
		{
			int remainingBudget = (m - sum);
			if (remainingBudget < 0)
			{
				break;
			}

			int budgetLimit = (remainingBudget / (n - i));
			int unusedBudget = 0;
			for (int j = 0; j < n; j++)
			{
				if (budgetLimit < budgets[j])
				{
					break;
				}
				else
				{
					unusedBudget += (budgetLimit - budgets[j]);
				}
			}

			int usedBudget = ((budgetLimit * n) - unusedBudget);
			if (usedBudget > maxBudget)
			{
				maxBudget = usedBudget;
				maxBudgetLimit = budgetLimit;
			}
			else if (usedBudget == maxBudget)
			{
				maxBudgetLimit = std::max(maxBudgetLimit, budgetLimit);
			}

			sum += budgets[i];
		}

		std::cout << maxBudgetLimit;
	}

	return 0;
}
