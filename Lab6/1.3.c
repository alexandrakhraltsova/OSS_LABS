#include <stdio.h>

extern char **environ;
int main(int argc, char *argv[])
{
    char **p;
    int count = 0;
	  const int MAX = 10;
    for(p = environ; *p != NULL && count < MAX; p++, count++)
      printf("%s\n", *p);
    return 0;
}
