// by bleepingmoon, 2014-05-04
// image-like structure without pointers

/* zad1 */
#include <stdio.h>
#define KANALY 3
#define WIERSZE 5
#define KOLUMNY 6

// pomocniczo, nie uzyte
void odwrocWiersz(int tab[], int rozmiar)
{
	int temp, i, j;
	for (i = 0, j = rozmiar - 1; i < j; i++, j--)
	{
		temp = tab[i];
		tab[i] = tab[j];
		tab[j] = temp;
	}
}

int main(void)
{

	// utworzenie tablicy i zmiennych pomocniczych A

	int obraz[KANALY][WIERSZE][KOLUMNY];
	int i, j, k, l, wartosc = 0;
	int temp;

	// zapelnianie danymi B

	for (i = 0; i < KANALY; i++)
	{
		for (j = 0; j < WIERSZE; j++)
		{
			for (k = 0; k < KOLUMNY; k++)
			{
				obraz[i][j][k] = wartosc++;
			}
		}
		
		wartosc = (i == 1) ? 1000 : 100;
	}

	printf("\nWypelniona tablica reprezentujaca obraz:\n\n");

	// wypisywanie C

	for (i = 0; i < KANALY; i++)
	{
		printf("Kanal nr: %d\n", i);
		for (j = 0; j < WIERSZE; j++)
		{
			for (k = 0; k < KOLUMNY; k++)
			{
				printf("%d ", obraz[i][j][k]);
			}
			printf("\n");
		}
	}

	// odbicie wzgledem osi pionowej D

	for (i = 0; i < KANALY; i++)
	{
		for (j = 0; j < WIERSZE; j++)
		{
			for (k = 0, l = KOLUMNY - 1; k < l; k++, l--)
			{
				temp = obraz[i][j][k];
				obraz[i][j][k] = obraz[i][j][l];
				obraz[i][j][l] = temp;
			}
		}
	}

	// ponowne wyswietlenie E

	printf("\nPo odbiciu wzgledem osi pionowej:\n\n");

	for (i = 0; i < KANALY; i++)
	{
		printf("Kanal nr: %d\n", i);
		for (j = 0; j < WIERSZE; j++)
		{
			for (k = 0; k < KOLUMNY; k++)
			{
				printf("%d ", obraz[i][j][k]);
			}
			printf("\n");
		}
	}

	return 0;
}
