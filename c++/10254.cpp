#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

int main()
{
    int T;
    std::cin >> T;
    while (T--)
    {
        long double max = 0.0;
        std::map< int, std::vector<int> > points;

        int n;
        std::cin >> n;
        while (n--)
        {
            int x, y;
            std::cin >> x >> y;
            if (points.find(x) == points.end())
            {
                std::vector<int> row;
                row.push_back(y);
                points.insert(std::pair< int, std::vector<int> >(x, row));
            }
            else
            {
                points[x].push_back(y);
            }
        }
        int x1, y1, x2, y2;
        long long distance_max = -1234567890;

        int column_min = 9876543210;
        int column_max = -1234567890;
        for (std::map< int, std::vector<int> >::iterator it = points.begin(); it != points.end(); ++it)
        {
            int column = it->first;
            std::vector<int> row = it->second;
            std::sort(row.begin(), row.end());
            if (column > column_max)
            {
                column_max = column;
            }
            if (column < column_min)
            {
                column_min = column;
            }
        }

        std::vector<int> left_row = points.begin()->second;
        std::vector<int> right_row = points.end()->second;
        int left_top = left_row[left_row.size() - 1];
        int left_bottom = left_row[0];
        int right_top = right_row[right_row.size() -1];
        int right_bottom = right_row[0];
        for (std::map< int, std::vector<int> >::iterator it = points.begin(); it != points.end(); ++it)
        {
            int column = it->first;
            std::vector<int> row = it->second;
            int left_y, right_y;
            for (std::vector<int>::iterator it = row.begin(); it != row.end(); ++it)
            {
                
            }
        }
        std::cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << std::endl;
    }
    return 0;
}