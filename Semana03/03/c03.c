/*Programa 3 
  Guilherme Gonzaga Silva
  11621EMT021
*/

#include <stdio.h>
#include <stdlib.h>

void hanoi(int n, char a, char b, char c)
{

if (n == 1) //1)
  printf("mova disco %d de %c para %c\n", n, a, b);
  else
  {
    hanoi(n - 1, a, c, b); //2)
    printf("mova disco %d de %c para %c\n", n, a, b); 
    hanoi(n - 1, c, b, a); //3)
  }
}
 
int main(int argc, char *argv[ ])
{
  int numDiscos; //numero de discos da torre
  numDiscos = atoi(argv[1]); //temos que o o numero de argumentos representa o numero discos 
  printf("\nPara #d discos, temos a seguinte resoluão: \n", numDiscos);
  hanoi(numDiscos, 'A', 'B', 'C'); //aplica a função para determinara solução 
  
  return 0;
}