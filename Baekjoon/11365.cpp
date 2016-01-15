#include<iostream>
#include<string>

int main()
{
	std::string line;
	do
	{
		std::getline(std::cin, line);
		if (!line.compare("END"))
		{
			break;
		}
		for (std::string::reverse_iterator rit = line.rbegin(); rit != line.rend(); ++rit)
		{
			std::cout << *rit;
		}
		std::cout << std::endl;
	} while (line.compare("END"));
	return 0;
}