#include <iostream>
#include <vector>
#include <algorithm>

typedef struct _Student
{
	int id;
	int understand;
	int knowledge;
} Student;

int main()
{
	int index = 0;
	int n;
	std::cin >> n;
	Student* students = new Student[n];
	for (int i = 0; i < n; ++i)
	{
		char situation;
		std::cin >> situation;
		if (situation == 'D')
		{
			int understand, knowledge;
			std::cin >> understand >> knowledge;
			Student* student = new Student;
			student->id = index;
			student->understand = understand;
			student->knowledge = knowledge;
			students[index++] = *student;
		}
		else
		{
			int id;
			std::cin >> id;
			Student student = students[id - 1];
			Student target = student;

			for (int j = 0; j < index; ++j)
			{
				Student cur = students[j];
				if (cur.id == student.id)
				{
					continue;
				}
				if (cur.knowledge == student.knowledge)
				{
					std::cout << cur.id << std::endl;
					break;
				}
				if ((cur.knowledge >= student.knowledge) && (cur.understand >= student.understand))
				{
					if (cur.knowledge < target.knowledge)
					{
						target = cur;
					}
					else if (cur.understand < target.understand)
					{
						target = cur;
					}
				}
			}

			if (target.id == student.id)
			{
				std::cout << "NE" << std::endl;
			}
			else
			{
				std::cout << target.id << std::endl;
			}
		}
	}
	return 0;
}