#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

long int p, q, t = 0, n, m, d, pp, pp2, M, C, flag = 0;
int a, b, i, j;
int count;
double em, en, en2;
double ez, ez2 = 5.0;
int i2 = 1;

int gcd(int a)
{
	int remainder = 2;
	int divident, divisor;

	for (i = 2; i < a; i++) {
		divident = a;
		divisor = i;
		while (divisor != 0) {
			remainder = divident % divisor;
			divident = divisor;
			divisor = remainder;
		}
		if (divident == 1) {
			printf("Relatively Prime Number is : %d \n", i);
		}
	}
	printf("\nChoose a number\n");
	scanf_s("%d", &pp);
	return pp;
}

double de(int m, int pp2)
{
	em = (i2 * m) + 1;
	en2 = em;
	en = em / pp2;
	ez = fmod(em, pp2);
	if (ez != 0) {
		i2++;
		return de(m, pp2);
	}
	return en;
}

int EncryKey(int d, int n) {
	int startM, x = 0, Cnew;
	printf("\nChoose a value for M: ");
	scanf_s("%d", &startM);
	x = pow(startM, d);
	Cnew = x % n;
	return Cnew;
}

int DecryKey(int C, int count, int n) {
	int Mnew, x = 0;
	x = pow(C, count);
	Mnew = x % n;
	return Mnew;
}

int main()
{
	printf("\nEnter the first prime number: ");
	scanf_s("%d", &p);
	t = p / 2;
	for (i = 2; i <= t; i++) {
		if (p % i == 0) {
			printf("\nYou entered a number which is not a prime\n");
			return main();
		}
	}
	m = 0;
	printf("\nEnter the second prime number: ");
	scanf_s("%d", &q);
	t = q / 2;
	for (i = 2; i <= t; i++) {
		if (q % i == 0) {
			printf("\nYou enterered a number which is not prime\n");
			return main();
		}
	}
	n = p * q;
	m = (p - 1) * (q - 1);
	count = gcd(m);
	d = de(m, count);
	C = EncryKey(d, n);
	M = DecryKey(C, count , n);
	printf("\nThe public key is {%d, %d}\n", count, n);
	printf("\nThe private key is {%d, %d}\n", d, n);
	printf("\nThe encypted is: %d\n", C);
	printf("\nThe decrypted is: %d\n", M);
	return 0;
}