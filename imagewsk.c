# by beepingmoon, 2014-05-04
# 3 dimensional array representing a sort of image
# very unreal, for test purposes only

#include <stdio.h>
#include <stdlib.h>
#define ROWS 6
#define COLS 5
#define CHANNELS 3

int main(void)
{
	// deklaracja jednej dlugiej tablicy i alokacja pamieci A
	int* image3d;
	int wartosc = 0;
	int length = CHANNELS * COLS * ROWS;
	//int matrix = COLS * ROWS;
	image3d = (int*) malloc(sizeof(int) * length);
	
	// wskaznik na poczatek tej tablicy
	int i;
	int* ptr;
	ptr = image3d;
	
	// wypelnienie danymi i poruszanie sie po tablicy liniowo B
	for (i = 0; i < length; i++)
	{
		*ptr = wartosc++;
		ptr++;
		if (i == 29)
		{
			wartosc = 100;
		}
		else if (i == 59)
		{
			wartosc = 1000;
		}
	}
	
	// odczytanie wpisanych wartosci w kolejnych komorkach pamieci C
	for (i = 0; i < length; i++)
	{
		if (i % 10 == 0)
		{
			printf("\n");
		}
		printf("%d ", *(image3d + i));
	}

	// 0-29 (1st channel RED), 30-59 (2nd channel GREEN), 60 - 89 (3rd channel BLUE)
	// wiersze: 0-4; 5-9; 10-14; 15-19; 20-24; 25-29;	
	printf("\n");

	// odbicie wzgledem osi pionowej D
	
	// ponowne wyswietlenie E

	return 0;
}
