#include<stdio.h>
#include<conio.h>
#include<math.h>


float u_cal(float u, int n)
{
	float temp = u;
	for (int i = 1; i < n; i++)
		temp = temp * (u - i);
	return temp;
}

int fact(int n)
{
	int f = 1;
	for (int i = 2; i <= n; i++)
		f *= i;
	return f;
}

void main()
{
    float x[100], y[100][100], sum, value, u, temp;
    int i, n, j, k=0, f, m;
    system("CLS");
    printf("\nHow many record ? ");
    scanf("%d", &n);
    for(i=0; i<n; i++)
    {
        printf("\n\nEnter the value of x%d: ", i);
        scanf("%f", &x[i]);
        printf("\n\n Enter the value of f(x%d): ", i);
        scanf("%f", &y[i][k]);
    }

    printf("\n\n Enter X for finding f(x): ");
    scanf("%f", &value);

    for(i=1; i<n; i++)
    {
        for(j=0; j<n-i; j++)
        {
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
        }
    }

    printf("\n__________________________________________________________________________________________________\n");
    printf("\n\tx(i)\t\ty(i)\t\ty1(i)\t\ty2(i)\t\ty3(i)\t\ty4(i)\t\t");
    printf("\n__________________________________________________________________________________________________\n");

    for(i=0; i<n; i++)
    {
        printf("\n %.3f", x[i]);
        for(j=0; j<n-i; j++)
        {
            printf("    ");
            printf("\t%.3f", y[i][j]);
        }
        printf("\n");
    }

    sum = y[0][0];
	u = (value - x[0]) / (x[1] - x[0]);
	for (int i = 1; i < n; i++) {
		sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);
	}

    printf("\n\n f(%.2f) = %f ", value, sum);
    printf("\n");
    system("PAUSE");
}
