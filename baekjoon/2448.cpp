/*
    2448 : 별 찍기 - 11
    URL : https://www.acmicpc.net/problem/2448
    Input :
        24
    Output :
                               *                        
                              * *                       
                             *****                      
                            *     *                     
                           * *   * *                    
                          ***** *****                   
                         *           *                  
                        * *         * *                 
                       *****       *****                
                      *     *     *     *               
                     * *   * *   * *   * *              
                    ***** ***** ***** *****             
                   *                       *            
                  * *                     * *           
                 *****                   *****          
                *     *                 *     *         
               * *   * *               * *   * *        
              ***** *****             ***** *****       
             *           *           *           *      
            * *         * *         * *         * *     
           *****       *****       *****       *****    
          *     *     *     *     *     *     *     *   
         * *   * *   * *   * *   * *   * *   * *   * *  
        ***** ***** ***** ***** ***** ***** ***** *****
*/

#include <iostream>

#define MAX_N 3072

bool matrix[MAX_N][MAX_N * 2];

void draw(int x, int y, int n)
{
    if (n == 3)
    {
        matrix[y][x + 2] = true;
        matrix[y + 1][x + 1] = true;
        matrix[y + 1][x + 3] = true;
        matrix[y + 2][x] = true;
        matrix[y + 2][x + 1] = true;
        matrix[y + 2][x + 2] = true;
        matrix[y + 2][x + 3] = true;
        matrix[y + 2][x + 4] = true;
    }
    else
    {
        int m = (n / 2);
        int x0 = x;
        int x1 = x + m;
        int x2 = x + n;
        int y0 = y;
        int y1 = y + m;

        draw(x1, y0, m);
        draw(x0, y1, m);
        draw(x2, y1, m);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    draw(0, 0, n);

    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < (n * 2); x++)
        {
            if (matrix[y][x])
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
