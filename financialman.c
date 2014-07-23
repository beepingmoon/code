#include <stdio.h>
#include <stdlib.h>
#define SIZE 1024

/*
by bleepingmoon, 2014-07-20
POJ 1004, Financial Management, http://poj.org/problem?id=1004
simply for fun
*/

int main(int argc, char* argv[])
{
	FILE* fp;
	char* buffer = (char*) malloc(SIZE);

	int numlines = 0;
	float sum = 0.0f;

	if (argc != 2) 
	{
		printf("Usage: %s filename.txt", argv[0]);
	}
	else
	{
		fp = fopen(argv[1], "r");
		if (fp == NULL)
		{
			printf("Remember about .txt file extension.");
			exit(EXIT_FAILURE);
		}
		while (fgets(buffer,SIZE,fp))
		{
			sum += atof(buffer);
			numlines++;
		}

		fclose(fp);
		printf("Average of %d numbers is %.2f.", numlines, sum/numlines);
	}
	return 0;
}
