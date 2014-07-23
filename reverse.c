// by beepingmoon, 2014-06-01
// testing time of reversing 1MB string

#include <string.h> // for strlen()
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
//#define SIZE 1024*1024

// reverse the given null-terminated string in place
void inplace_reverse(char * str)
{
  if (str)
  {
    char * end = str + strlen(str) - 1;

    // swap the values in the two given variables
    // XXX: fails when a and b refer to same memory location

    #define XOR_SWAP(a,b) do\
    {\
      a ^= b;\
      b ^= a;\
      a ^= b;\
    } while (0)

    // walk inwards from both ends of the string, 
    // swapping until we get to the middle
    while (str < end)
    {
      XOR_SWAP(*str, *end);
      str++;
      end--;
    }
    #undef XOR_SWAP
  }
}

int main(int argc, char* argv[])
{
  FILE* tfile;
  tfile = fopen("random.txt","rb"); /* opening for reading */

  clock_t begin, end;
  double time_spent;

  /* saving length of file and reading it to memory */
  fseek(tfile, 0, SEEK_END);
  long pos = ftell(tfile);
  fseek(tfile, 0, SEEK_SET);

  char *bytes = malloc(pos);
  fread(bytes, pos, 1, tfile);
  fclose(tfile);  /* closing file */

  /* measuring time */

  struct timeval tv1, tv2;
  gettimeofday(&tv1, NULL);
  
  strrev(bytes);
  
  gettimeofday(&tv2, NULL);

  printf("Total time = %f seconds\n",
    (double) (tv2.tv_usec - tv1.tv_usec) / 1000000 +
    (double) (tv2.tv_sec - tv1.tv_sec));

  /* reversing string and measuring time of execution */
  /*
  begin = clock();

  inplace_reverse(bytes);

  end = clock();
  time_spent = ((double)end - (double)begin) / CLOCKS_PER_SEC;

  printf("Time spent: %f", time_spent);
  */
  return 0;
}
