#include<iostream>
#include<string>
/*
월 목 목 일
화 금 금 일
수 월 목 토
*/
int first_date(int month)
{
	switch (month)
	{
	case 2:
	case 3:
	case 11:
		return 4;
	case 1:
	case 10:
		return 1;
	case 4:
	case 7:
		return 0;
	case 5:
		return 2;
	case 8:
		return 3;
	case 6:
		return 5;
	case 9:
	case 12:
		return 6;
	}
}
/*
SUN, MON, TUE, WED, THU, FRI, SAT
*/
char* to_str(int date)
{
	switch (date)
	{
	case 0:
		return "SUN";
	case 1:
		return "MON";
	case 2:
		return "TUE";
	case 3:
		return "WED";
	case 4:
		return "THU";
	case 5:
		return "FRI";
	case 6:
		return "SAT";
	}
}

char* parse(int month, int day)
{
	int date = first_date(month);
	date += (day % 7) - 1;
	if (date == -1)
	{
		date = 6;
	}
	date %= 7;
	return to_str(date);
}

int main()
{
	int month, day;
	scanf("%d %d", &month, &day);
	printf("%s", parse(month, day));
	return 0;
}