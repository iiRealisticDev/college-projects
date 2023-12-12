#include <stdio.h>

int main()
{
  // get an integer from user
  int n;
  printf("Enter an integer: ");
  scanf("%d", &n);

  if (n >= 20)
    printf("20 or more\n");
  else if (n >= 10)
    printf("10 or more\n");
  else
    printf("0\n");
}