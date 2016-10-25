#include <iostream>

int main()
{
	double temperature = 999;
	double* save = NULL;
	do
	{
		std::cin >> temperature;
		if (save != NULL && temperature != 999)
		{
			printf("%.2lf\n", (temperature - *save));
		}
		else
		{
			save = new double;
		}
		*save = temperature;
	} while (temperature != 999);
	return 0;
}