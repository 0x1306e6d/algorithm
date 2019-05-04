/*
    11365 : !밀비 급일
    URL : https://www.acmicpc.net/problem/11365
    Input :
		!edoc doog a tahW
		noitacitsufbo
		erafraw enirambus detcirtsernu yraurbeF fo tsrif eht no nigeb ot dnetni eW
		lla sees rodroM fo drol eht ,ssertrof sih nihtiw delaecnoC
		END
    Output :
        What a good code!
        obfustication
        We intend to begin on the first of February unrestricted submarine warfare
        Concealed within his fortress, the lord of Mordor sees all
*/

#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
	std::string line;

	while (true)
	{
		std::getline(std::cin, line);
		if (!line.compare("END"))
		{
			break;
		}
		for (std::string::reverse_iterator rit = line.rbegin();
			 rit != line.rend();
			 ++rit)
		{
			std::cout << *rit;
		}
		std::cout << std::endl;
	}

	return 0;
}