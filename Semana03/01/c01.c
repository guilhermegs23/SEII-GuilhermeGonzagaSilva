#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "c01.h"

struct complexo;
 
int main(void)
{
    struct complexo x, y, *pz, *ps, *pd, *pm;//, *pc_1, *pc_2;
    printf("\n Z1: \n");
    leiaComplexo(&x);
    printf("Z2: \n");
    leiaComplexo(&y);
    pz = somaComplexos(&x, &y);
    ps = subComplexos(&x, &y);
    pd = divComplexos(&x, &y);
    pm = multiComplexos(&x, &y);
    /*pc_1 = convComplexos(&x);
    pc_2 = convComplexos(&y);*/

    
    printf("\n\nAs operações com os complexos são: \n");
    printf("\nZ1 + Z2 = ");
    escrevaComplexo(pz);
    putchar('\n');
    printf("Z1 - Z2 = ");
    escrevaComplexo(ps);
    putchar('\n');
    printf("Z1 / Z2 = ");
    escrevaComplexo(pd);
    putchar('\n');
    printf("Z1 * Z2 = ");
    escrevaComplexo(pm);
    putchar('\n');
    /*printf("A forma pola de Z1 eh: ");
    escrevaPolar(pc_1);
    putchar('\n');
    printf("A forma pola de Z2 eh: ");
    escrevaPolar(pc_2);
    putchar('\n');
*/

    return 0;
}

