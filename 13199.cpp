/*
    13199 : 치킨 먹고 싶다
    URL : https://www.acmicpc.net/problem/13199
    Input :
        2
        10000 50000 5 1
        10000 250000 5 1
    Output :
        0
        1
*/
#include <iostream>

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int P, M, F, C;
        scanf("%d %d %d %d", &P, &M, &F, &C);
        int coupon_D = (M / P) * C;
        int coupon_S = (M / P) * C;
        int chicken_D = coupon_D / F;
        int chicken_S = 0;
        while (coupon_S >= F)
        {
            int new_chicken = coupon_S / F;
            coupon_S = coupon_S % F;
            coupon_S = coupon_S + (new_chicken * C);
            chicken_S = chicken_S + new_chicken;
        }
        printf("%d\n", (chicken_S - chicken_D));
    }
    return 0;
}